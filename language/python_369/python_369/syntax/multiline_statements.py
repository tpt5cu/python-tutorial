# https://stackoverflow.com/questions/38125328/what-does-a-backslash-by-itself-mean-in-python


'''
The backslash "\" makes it so that Python parses a statement that is split over two lines as if it were on one line
- parentheses also work
- curly braces (set literal) and brackets (list literal, or comprehension, etc.) also extend over multiple lines, but they have special meanings,
  unlike the general application of parentheses and backslashes
'''

def multiline_if():
    if 1 == 1 and \
        2 == 2 and \
            3 == 3:
        print('It works!') # It works!


def multiline_arithmetic():
    '''I thought using parentheses was only for extending string literals across multiple lines, but it's more general than that'''
    x = (1 + 1 +
        2 + 3
        + 4)
    print('x: {}'.format(x)) # x: 11


if __name__ == '__main__':
    #multiline_if()
    multiline_arithmetic()