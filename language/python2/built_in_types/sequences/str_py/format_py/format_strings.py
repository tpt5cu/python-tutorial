# https://realpython.com/python-string-formatting/
# https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting - shows the printf format specifier flags


from string import Template


def old_format_specifier():
    """The old format specifier % can be used positionally or with keywords. The format specifier flags are essential"""
    cat = 'Jumbo'
    print('I love my cat %s' % cat) # I love my cat Jumbo
    print('I love my cat %(cat)') # I love my cat %(cat)
    print('I love my cat %(cat)s' % {'cat': cat}) # I love my cat Jumbo
    num = 3.2
    print('I like the number %d' % num) # 3
    print('I like the number %f' % num) # 3.2000000


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


def new_format_function():
    """The new format specifier has slightly nicer syntax than the old style. It should be used when possible"""
    color = 'maroon'
    other = 'black'
    # Implicit positional syntax
    print('{} is a weird color, but I like {}'.format(color, other)) # maroon is a weird color, but I like black
    # Explicit positional syntax
    print('{1} is a weird color, but I like {0}'.format(color, other)) # black is a weird color, but I like maroon
    # keyword syntax
    print('{c1} is a weird color, but I like {c2}'.format(c1=color, c2=other)) # maroon is a weird color, but I like black


def string_interpolation():
    """Not available until Python 3.6"""


def template_strings():
    """Must import the Template class to use it"""
    string = Template("Hello $name").substitute(name="Austin")
    print(string) # Hello Austin


if __name__ == "__main__":
    #old_format_specifier()
    #new_format_function()
    template_strings()