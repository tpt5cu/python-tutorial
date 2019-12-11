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
    # This is invalid syntax
    #string3 = "yes" + 
    #"no"
    #print(string3)
    string = """Triple quotes
    can be used
    for strings that span
    multiple lines However, the strings will have the newlines and spacing inside of them."""
    print(string)
    # This works because string literals that are part of a single expression and only have whitespace between them will be implicitly converted into
    # a single string literal
    # - The parentheses form an expression that contains the string literals
    # - Be careful not to include commas or I'll be printing a tuple
    # - 
    string2 = ("Strings can be written"
               " in this way"
               " to avoid including spaces and newlines in the format.")
    print(string2)


def returned_strings():
    '''
    When using strings that are returned from function calls, I must use the "+" string concatenation operator.
    - Recall that the concatenation operator "+" never works across two lines
    - I promise that the "+" operator is NOT optional in this case
    - The \ operator also cannot be used
    '''
    def get_string():
        return "cool string!"
    long_string = (get_string() + get_string() +
        get_string() + "Yo" + get_string())
    print(long_string)
    # This syntax can only be used with literals, not functions that return strings
    string4 = "Strings can be " \
        "split across multiple" \
        " lines without including newlines this way"
    print(string4)


def raw_string():
    """Precede a string literal with 'r' or 'R' to create a raw string. Very useful for regular expressions."""
    string = r"I'm a raw string \\ so \" nothing \t gets \u escaped."
    print(string)


def string_with_newlines():
    """There is no way to write a string literal across multiple lines without parenthesis (or triple quotes)"""
    # This is valid syntax, but only the first literal is assigned to the variable. The other literal is ignored
    string = 'first line'
    'second line'
    print(string)
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
    #returned_strings()
    #raw_string()
    string_with_newlines()