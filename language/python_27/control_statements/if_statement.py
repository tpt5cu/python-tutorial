def compound_comparison(x):
    '''Compound comparisons like this are not valid in other languages, but are valid in Python'''
    if 1 < x < 5:
        print(x)
    else:
        print(False)


def if_statement_variable():
    '''There is no such thing as an if-statement variable. Check the surrounding context for the variable'''
    if x < 5:
        print(x)


def perform_compound_comparison():
    compound_comparison(0) # False
    compound_comparison(4) # 4


if __name__ == '__main__':
    #perform_compound_comparison()
    if_statement_variable()