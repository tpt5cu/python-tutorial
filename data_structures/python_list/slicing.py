

def negativeSlice():
    string = "Avocado"
    """prints "o" because a negative index gets elements starting from the right side of the list-like object"""
    print(string[-1])
    """prints "Avoc" because we start at the beginning of the string, then go up to (but not including) the -3 element, 
    which is 'a'
    """
    print(string[:-3])
    """prints  'ado' because we start at the negative 3rd element, which is 'a', and go to the end of the list"""
    print(string[-3:])


if __name__ == "__main__":
    negativeSlice();