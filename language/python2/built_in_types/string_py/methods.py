"""
https://docs.python.org/2/library/stdtypes.html#string-methods - built-in methods on str objects
https://docs.python.org/2/library/stdtypes.html#sequence-types-str-unicode-list-tuple-bytearray-buffer-xrange - sequence-type methods that all sequence types (including strings) support
https://docs.python.org/2/library/string.html - the string module (not same as built-in str)
"""


import re


def strip_py():
    """ Use <string>.strip() to remove the specified characters from the leading and trailing ends of the string.
    CAUTION: ALL such specified characters will be removed! """
    # The first 'o', the last 'd', and ".omd" will be removed
    string = "oOoy, what a nice string you created.omd".strip(".omd")
    print(string)


def rstrip_py():
    """ 
    print() automatically inserts a newline, so sometimes it's useful to strip off an existing newline
    """
    line = "This line has a newline\n"
    print(line.rstrip("\n"))
    print("no extra space above")
    

def replace_py():
    """ replace() can also take a number specifying the number of time to replace a pattern, starting from the beginning of the string """
    # This line throws an error. Also, I can't escape the forward slash!
    #string = 'What a cool \/ file name.txt'
    string = 'What a cool/file name.txt'.replace("/", ":")
    with open(string, "w") as f:
        f.write(string)


def find_py():
    """ find() returns the index of the substring, or -1 if it isn't found """
    string = "Hi there"
    print(string.find("z"))


def regex_find():
    """
    This doesn't belong here, but that's okay. Use re.search() to search the entire string for any occurance of <re>. Use re.match() to only search
    from the beginning of the string.
    """
    string = "Hello567There"
    mo = re.search(r"\d{3}", string)
    print(mo.group(0))


def equals():
    """ Just use == to compare strings """
    my_str = "hello there"
    print(my_str == "hello there\n") # False
    print(my_str.startswith("hello there\n")) # False
    print(my_str.startswith("hello there")) # True
    print(my_str == "hello there") # True


def split_py():
    filename = "myfilename.java"
    filename = filename.split(".")[0] + ".py"
    print(filename)

if __name__ == "__main__":
    #strip_py()
    #rstrip_py()
    #find_py()
    #regex_find()
    #equals()
    split_py()