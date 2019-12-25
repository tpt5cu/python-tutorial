# https://realpython.com/python-string-formatting/
# https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting - shows the printf format specifier flags


from string import Template


def old_format_specifier():
    '''The old format specifier % can be used positionally or with keywords. The format specifier flags are essential'''
    cat = 'Jumbo'
    print('I love my cat %s' % cat) # I love my cat Jumbo
    print('I love my cat %(cat)') # I love my cat %(cat)
    print('I love my cat %(cat)s' % {'cat': cat}) # I love my cat Jumbo
    num = 3.2
    print('I like the number %d' % num) # 3
    print('I like the number %f' % num) # 3.2000000


def new_format_function():
    '''The new format specifier has slightly nicer syntax than the old style. It should be used when possible'''
    color = 'maroon'
    other = 'black'
    # Implicit positional syntax
    print('{} is a weird color, but I like {}'.format(color, other)) # maroon is a weird color, but I like black
    # Explicit positional syntax
    print('{1} is a weird color, but I like {0}'.format(color, other)) # black is a weird color, but I like maroon
    # keyword syntax
    print('{c1} is a weird color, but I like {c2}'.format(c1=color, c2=other)) # maroon is a weird color, but I like black


def new_format_function_type_coercion():
    '''
    The format() function will implicitly call str() on non-string arguments
    - If a format argument isn't specified, the string will contain "{}"
    '''
    print('Most months have {} days'.format(30)) # Most months have 30 days
    print('Python calls booleans {}'.format(bool)) # Python calls booleans <type 'bool'>
    print('{}.txt') # {}.txt


def template_strings():
    '''Must import the Template class to use it'''
    string = Template('Hello $name').substitute(name='Austin')
    print(string) # Hello Austin


if __name__ == '__main__':
    #old_format_specifier()
    #new_format_function()
    new_format_function_type_coercion()
    #template_strings()