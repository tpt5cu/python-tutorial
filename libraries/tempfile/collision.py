import tempfile

"""
tempfile does not allow me to purposefully cause name collisions. The prefix and suffix options merely restrict the name of the temporary directory to
start and end with certain characters. I cannot fully set the name.

Since I cannot set the generated name used by tempfile, I cannot conclude whether or not multiple processes, each creating temporary
directories, have the potential to create identical directory names and cause a collision.
"""

def name_collision():
    temp_dir = tempfile.mkdtemp(dir=".", prefix="hello", suffix="goodbye")
    #/Users/austinchang/tutorials/python/libraries/tempfile/tmp7mfguh0e

if __name__ == "__main__":
    name_collision()