# https://stackoverflow.com/questions/6159900/correct-way-to-write-line-to-file
# https://stackoverflow.com/questions/1466000/python-open-built-in-function-difference-between-modes-a-a-w-w-and-r

"""
 The argument mode points to a string beginning with one of the following
 sequences (Additional characters may follow these sequences.):

 ``r''   Open text file for reading.  The stream is positioned at the
         beginning of the file.

 ``r+''  Open for reading and writing.  The stream is positioned at the
         beginning of the file.

 ``w''   Truncate file to zero length or create text file for writing.
         The stream is positioned at the beginning of the file.

 ``w+''  Open for reading and writing.  The file is created if it does not
         exist, otherwise it is truncated.  The stream is positioned at
         the beginning of the file.

 ``a''   Open for writing.  The file is created if it does not exist.  The
         stream is positioned at the end of the file.  Subsequent writes
         to the file will always end up at the then current end of file,
         irrespective of any intervening fseek(3) or similar.

 ``a+''  Open for reading and writing.  The file is created if it does not
         exist.  The stream is positioned at the end of the file.  Subse-
         quent writes to the file will always end up at the then current
         end of file, irrespective of any intervening fseek(3) or similar.
"""

def get_parent_dir_path(target_dir):
    # It should be a valid string, but if it's not then an error will (correctly) be thrown
    target_dir = str(target_dir)
    if not target_dir.endswith("/"):
        target_dir += "/"
    # Get the absolute path of this module
    this_module = str(__file__)
    # Get the index where the target_dir ends in the path
    idx = this_module.find(target_dir) + len(target_dir)
    # slice the path to get the part I want
    path = this_module[:idx]
    # print(this_module)
    # print(path)
    return path


def write_lines():
    with open(get_parent_dir_path("python_tutorial") + "temp.txt", mode="w+", encoding="utf-8") as file:
        for x in range(100):
            file.write(str(x) + "\n")
    print("File was overwritten")


if __name__ == "__main__":
    # get_parent_dir_path("python_tutorial/")
    write_lines()
