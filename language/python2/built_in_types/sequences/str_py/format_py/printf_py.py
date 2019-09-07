def old_school_variable_substitution():
    """ The character after the % in a string is the format specifier. %d is decimal, %f is float, %x is hex. There are several. """
    food = "chocolate"
    print "My favorite food is %s" % food
    # If I want to do multiple substitutions, then I need to wrap the variables because the % argument only takes one argument
    print "The first 3 natural numbers are %d, %f, %x" % (1, 2, 3)
    # Format string substitution is also possible with named values, but its quite verbose
    one = -1
    two = -2
    three = -3
    print("The first three negative integers are %(one)d, %(two)d, %(three)d" % {"one": one, "two": two, "three": three})


def in_depth_printf_formatting():
    """
    printf-style string formatting actually has 7 components, which must appear in order.
    1) % character which marks start of a format specifier. (required)
    2) A mapping key enclosed in parentheses (e.g. %(one)) for the sake of mapping. (optional)
    3) Conversion flags: #, 0, -, ' ', +. See docs because a few of these are weird. (optional)
        - #: Use alternative form (see docs)
        - 0: Zero pad a numeric value if needed
        - -: Left adjust 
        - ' ': insert a blank space
        - +: Value should be preceeded by a sign character (+/-)
    4) Minimum field width. See docs (optional)
    5) Precision. See docs (optiona)
    6) Length modifier (optional)
    7) Conversion type. These are things like the 'd' in "%d". (required)
    """
    print("This is the number 1: %d" % (1))
    print("This is the number 1: %5d" % (1)) # minimum field width
    print("This is the number 1: %.5d" % (1)) # precision
    print("This is the number 1: %8.5d" % (1)) # minimum field width and precision