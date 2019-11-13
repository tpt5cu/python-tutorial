# https://stackoverflow.com/questions/20202418/why-is-the-cmp-parameter-removed-from-sort-sorted-in-python3-0


class Toothpaste(object):

    def __init__(self, name, price, taste):
        self.name = name
        self.price = price
        self.taste = taste

    def __repr__(self):
        return self.name


def compare_toothpastes():
    '''
    I want to compare toothpastes based on price and taste [1, 5] scale. 
    '''
    colgate = Toothpaste('colgate', 3.99, 4)
    crest = Toothpaste('crest', 3.99, 3)
    generic = Toothpaste('generic', 3.99, 1)
    print(crest < colgate) # Python 3 TypeError
    toothpastes = [crest, generic, colgate]
    sorted_toothpastes = sorted(toothpastes)
    print(sorted_toothpastes)


if __name__ == '__main__':
    compare_toothpastes()