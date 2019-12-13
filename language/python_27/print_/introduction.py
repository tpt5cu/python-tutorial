'''
With commas, separate arguments are passed to the print() function, and each argument gets printed separately. print() also happens to insert a single
space between each argument.
'''


def print_with_commas():
    '''
    These two lines print completely different things in Python 2. In Python 3, the first line is an error and the second line prints the same thing
    as the first line in Python 2!
    '''
    # - Python 2: ('hello', 'there', 'general', 'kenobi')
    # - Python 3: hello there general kenobi
    print("hello", "there", "general", "kenobi")
    # Python 2: hello there general kenobi
    # Python 3: SyntaxError
    #print "hello", "there", "general", "kenobi" 


if __name__ == "__main__":
    print_with_commas()