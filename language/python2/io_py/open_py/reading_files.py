# https://docs.python.org/2/library/stdtypes.html#bltin-file-objects
# https://stackoverflow.com/questions/8945370/garbage-in-file-after-truncate0-in-python - how truncate really works


import os, re


src_path = os.path.join(os.path.dirname(__file__), "test-files/test-text.txt")
target_path = os.path.join(os.path.dirname(__file__), "test-files/new-file.txt")


def read_line():
    """
    When thinking about the size of a line, think in terms of the number of characters, not what my editor is displaying.
    - readline() includes the newline '\n' at the end of a line
    - simple-no-newline.txt has a size of 4 bytes. There are 4 characters and no newline
    - simple-yes-newline.txt has a size of 15 bytes. There are 12 characters and 3 newlines.
    - The len() of a 4-character line without a newline is 4
    - The len() of a 4-character line with a newline is 5
    - The len() of a 1-character line that only consists of a newline is 1
    """
    for filename in ['test-files/simple-no-newline.txt', 'test-files/simple-yes-newline.txt']:
        filepath = os.path.join(os.path.dirname(__file__), filename)
        print(os.path.getsize(filepath))
        with open(filepath) as f:
            for line in f:
                print(len(line))


def read_lines():
    """
    readlines() uses readline() to insert all of the lines into a list! This won't work for really large files, but it's convenient. The counterpart
    to readlines() is writelines().
    - readlines() is different from read() in that read() returns a string.
    """
    with open(src_path) as f:
        lines = f.readlines()
    with open(target_path, 'w') as f:
        f.writelines(lines)


def use_iterator():
    """
    A Python file object is its own iterator. That means its next() method is implicitly called when used in a for-loop. This is quite efficient.
    Since next() uses a hidden read-ahead buffer for efficiencey, combining next() (and hence using a for-loop) with other methods like readline()
    doesn't work correctly. However, seek() can be used with an absolute position will flush the read-ahead buffer.
    """
    with open(target_path, 'w') as fw:
        with open(src_path) as f:
            for line in f:
                # Skip lines with numbers for fun
                if re.search(r"\d", line) is None:
                    fw.write(line)


def inplace_modification():
    """ 
    It is possible to modify a file in-place with 'r+' mode, but it's easier to use the fileinput module. There are two main approaches:
    1) Read the entire file into memory, modify it, and write the modified data back into the file. This isn't efficient but is easy
    2) Read the file line by line. If a line has something I want to modify, modify that line, seek() back to the beginning of the line, and write the
       modified content
        - Ideally, the length of the new content will be EXACTLY equal to the the length of the content that is being replaced. If it isn't, then I'll
          overwrite other content in the file! To avoid doing THAT, I would have to read the entire file into memory beforehand, which would defeat
          the entire purpose of doing this. I could also do something crazy complicated like comparing the length of the new line to the old line,
          then reading the part of the file that would be overwritten, then somehow shuffling the rest of the file forwards but that's crazy
    """
    #print("file size: " + str(os.path.getsize(target_path))) # 739
    cumulative_line_length = 0
    with open(target_path, 'r+') as f:
        #print(f.tell()) # 0
        for line in f:
            print('line length: ' + str(len(line)))
            #print(f.tell()) # Always 739 because of the read-ahead buffer which is presumably large
            if line.find('code') != -1:
                new_line = line.replace('code', 'book')
                #new_line = line.replace('code', 'fruit loops and honey nut cheerios')
                f.seek(cumulative_line_length, os.SEEK_SET) # Adjust the file descriptor positioning with an absolute value
                print('Position after seek: ' + str(f.tell()))
                f.write(new_line)
            cumulative_line_length += len(line)
    print('cumulative line length: ' + str(cumulative_line_length)) # 739


def truncate_file():
    """
    <file object>.truncate([size]) does NOT automatically truncate the file to 0 bytes! By default, it truncates to the current location of the file
    descriptor. If I set size = 0, then it will truncate the file to at most 0 bytes.
    """
    read_lines()
    with open(target_path, 'r+') as f:
        # This will truncate to 0 bytes because the file descriptor happens to be at the start of the file
        #f.truncate() 
        # This will truncate everything after the first 10 characters
        #f.seek(10, os.SEEK_SET); f.truncate() 
        # This will truncate the file to at most 20 bytes
        #f.truncate(20) 

        # The file pointer's current position isn't affected by truncate(). Thus, if the file pointer is at the end of the file, and then the file is
        # truncated to 0 bytes, the file pointer will still be at the end of the file!
        print(os.path.getsize(target_path)) # 2289
        f.seek(0, os.SEEK_END) # go to end of the file
        print(f.tell()) # 2289
        f.truncate(0)
        print(os.path.getsize(target_path)) # 0
        print(f.tell()) # 2289
        # This write corrupts the file!
        #f.write("some nice text")
        # This write is okay
        f.seek(0) # go to the beginning of the file
        f.write("some nice text")


def truncate_file_order():
    """
    It does not matter whether seek() is called after or before truncate(), just make sure to move the file pointer to the start of the file when
    writing after truncate()
    """
    read_lines()
    #with open(target_path, 'r+') as f:
    #    f.truncate(0)
    #    f.seek(0)
    #    f.write("Some new input")
    with open(target_path, 'r+') as f:
        f.seek(0)
        f.truncate(0)
        f.write("Some other new input")


def rename_while_open():
    """
    Apparently renaming a file while it's open is okay, both for reading and writing!
    """
    with open(target_path, 'w') as f:
        f.write("renamed_while_open() wrote some content to this file")
    head = os.path.split(target_path)[0]
    new_name = os.path.join(head, 'renamed-file.txt')

    def rename_without_with():
        f = open(target_path, 'r+')
        print(f.read())
        os.rename(target_path, new_name)
        f.seek(0)
        print(f.read())
        f.write("rename_without_with()")
        f.close()

    def rename_with_with():
        with open(target_path, 'r+') as f:
            print(f.read())
            os.rename(target_path, new_name)
            f.seek(0)
            print(f.read())
            f.write("rename_with_with()")

    def online_example():
        """
        https://stackoverflow.com/questions/6697972/update-file-descriptor-after-os-rename
        - This example claims that this code should result in a bad file descriptor, but it doesn't. Actually, it's because that person used a 'rw'
          mode, which isn't a valid file mode. That's the ONLY reason they got a bad file descriptor
        """
        f = open(target_path, 'r+')
        #f = open(target_path, 'rw') # Bad file descriptor
        os.rename(f.name, f.name + ".bak")
        f.write('test')
        f.close()

    #rename_without_with()
    #rename_with_with()
    online_example()
    #os.remove(new_name)


if __name__ == "__main__":
    #read_line()
    #read_lines()
    #use_iterator()
    # Use both together
    #use_iterator() # reset the content
    #inplace_modification()
    #truncate_file()
    #truncate_file_order()
    rename_while_open()