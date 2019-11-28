def compound_comparison(x):
    '''Compound comparisons like this are not valid in other languages, but are valid in Python'''
    if 1 < x < 5:
        print(x)
    else:
        print(False)


def perform_compound_comparison():
    compound_comparison(0) # False
    compound_comparison(4) # 4


if __name__ == '__main__':
    perform_compound_comparison()