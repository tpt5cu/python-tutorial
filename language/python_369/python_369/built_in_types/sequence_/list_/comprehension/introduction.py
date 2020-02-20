def leaked_comprehension_variables():
    '''Python 3 no longer allows comprehension variables to leak into the enclosing scope'''
    summed = [x + 4 for x in (1, 2, 3)]
    print(summed) # [5, 6, 7]
    print(x) # NameError


def naked_tuples():
    '''
    Python 3 no longer allows tuples without parentheses inside of list comprehensions
    - Naked tuples by themselves are fine
    '''
    #summed = [x + 4 for x in 1, 2, 3] # SyntaxError
    #print(summed)
    t = 1, 2, 3
    print(t)


if __name__ == '__main__':
    #leaked_comprehension_variables()
    naked_tuples()