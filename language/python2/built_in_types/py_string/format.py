"""
https://stackoverflow.com/questions/11630106/advanced-string-formatting-vs-template-strings
https://realpython.com/python-string-formatting/
https://stackoverflow.com/questions/599625/python-string-prints-as-ustring
"""

def string_interpolation():
    """ Not available until Python 3.6.
    """
    pass

def string_literals():
    """strings can be delineated with single, double, or triple quotes."""
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

def inserting_variables():
    name = "Austin"
    string = "Hello my name is {} and I like {}.".format(name, "cats")
    print(string)
    # Very useful when substituting the same variable multiple times
    string = "Hello my name is {name}. I was named {name} because my parents liked the name {name}.".format(name=name)
    print(string)
    # This is the most basic way, but it's annoying to have to remember to put spaces around the end quotations.
    string = "Hello my name is " + name
    print(string)


def raw_string():
    """Precede a string literal with 'r' or 'R' to create a raw string."""
    string = r"I'm a raw string \\ so \" nothing \t gets \u escaped."
    print(string)

if __name__ == "__main__":
    #string_interpolation()
    #string_literals()
    #multiline_strings()
    inserting_variables()
    #raw_string()
