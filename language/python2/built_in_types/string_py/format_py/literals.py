"""
https://stackoverflow.com/questions/11630106/advanced-string-formatting-vs-template-strings
https://realpython.com/python-string-formatting/ - types of string templating
https://stackoverflow.com/questions/599625/python-string-prints-as-ustring
https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting
"""

def string_interpolation():
    """ Not available until Python 3.6.
    """
    pass


def types_of_quotes():
    """ strings can be delineated with single, double, or triple quotes. """
    string1 = "I am a cool string!"
    string2 = 'I am also a cool string.'
    """Use the backslash for escape sequences."""
    string3 = "This string can have \"quotes\" inside of it."
    print(string3)
    print(str(type(string3)))


def multiline_strings():
    string = """Triple quotes
    can be used
    for strings that span
    multiple lines However, the strings will have the newlines and spacing inside of them."""
    print(string)
    string2 = ("Strings can be written"
               " in this way"
               " to avoid including spaces and newlines in the format.")
    print(string2)
    # This is invalid syntax
    #string3 = "yes" + 
    #"no"
    #print(string3)


def raw_string():
    """
    Precede a string literal with 'r' or 'R' to create a raw string. Very useful for regular expressions.
    """
    string = r"I'm a raw string \\ so \" nothing \t gets \u escaped."
    print(string)


if __name__ == "__main__":
    #string_interpolation()
    #string_literals()
    multiline_strings()
    #raw_string()