"""
https://docs.python.org/2/library/stdtypes.html#string-methods - built-in methods on str objects
https://docs.python.org/2/library/stdtypes.html#sequence-types-str-unicode-list-tuple-bytearray-buffer-xrange - sequence-type methods that all sequence types (including strings) support
https://docs.python.org/2/library/string.html - the string module (not same as built-in str)
"""

def py_strip():
    """ Use <string>.strip() to remove the specified characters from the leading and trailing ends of the string.
    CAUTION: ALL such specified characters will be removed! """
    # The first 'o', the last 'd', and ".omd" will be removed
    string = "oOoy, what a nice string you created.omd".strip(".omd")
    print(string)

def py_replace():
    # Throws an error. Also, I can't escape the forward slash!
    #string = 'What a cool \/ file name.txt'
    string = 'What a cool/file name.txt'.replace("/", ":")
    with open(string, "w") as f:
        f.write(string)

if __name__ == "__main__":
    #py_strip()
    py_replace()