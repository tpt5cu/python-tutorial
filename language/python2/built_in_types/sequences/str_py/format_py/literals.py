# https://stackoverflow.com/questions/11630106/advanced-string-formatting-vs-template-strings
# https://realpython.com/python-string-formatting/ - types of string templating
# https://stackoverflow.com/questions/599625/python-string-prints-as-ustring
# https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting


def types_of_quotes():
    """strings can be delineated with single, double, or triple quotes."""
    string1 = "I am a cool string!"
    string2 = 'I am also a cool string.'
    # Use the backslash for escape sequences.
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
    # Apparently, this syntax can only be used with literals, not functions that return strings
    string4 = "Strings can be " \
        "split across multiple" \
        " lines without including newlines this way"
    print(string4)


def single_line_string_across_multiple_lines():
    """
    Parentheses can be used to write a string literal across multiple lines but have it print as a single line.
    - Be careful not to include commas or I'll be printing a tuple!
    - If I'm getting strings that are returned from function calls, I need the '+' operator to concatenate those returned strings, regardless of
      whether or not the function call is on a new line
    """
    long_string = ('First line. '
    'second line. ' 'second line part 2'
    'third line.')
    print(long_string) # First line. second line. second line part 2third line.
    def get_string():
        return "cool string!"
    long_string = (get_string() + get_string() + 
        get_string() + "Yo" + get_string())
    print(long_string) # cool string!cool string!cool string!Yocool string!
    # This is invalid syntax. The parentheses are needed
    #bad_string = get_string() + get_string() +
    #    get_string()
    #print(bad_string)


def raw_string():
    """Precede a string literal with 'r' or 'R' to create a raw string. Very useful for regular expressions."""
    string = r"I'm a raw string \\ so \" nothing \t gets \u escaped."
    print(string)


def string_with_newlines():
    """There is no way to write a string literal across multiple lines without parenthesis (or triple quotes)"""
    # This is valid syntax, but does not combine the string literals
    #string = 'first line'
    #'second line'
    # This is invalid syntax
    #string = 'first line ' +
    #    'second line'
    # This is also invalid syntax
    #string = "first line
    #    second line"
    # This is one way to write a multiline string literal, but it's very ugly
    string = """first line
    second line"""
    print(string)


if __name__ == "__main__":
    #types_of_quotes()
    #multiline_strings()
    #single_line_string_across_multiple_lines()
    #raw_string()
    string_with_newlines()