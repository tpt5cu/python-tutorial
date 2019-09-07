# https://docs.python.org/2.7/reference/datamodel.html#the-standard-type-hierarchy - there is a subsection on sets near the top


def no_indexing():
    """Sets are by definition unordered, so they cannot be indexed! They can be iterated over"""
    my_set = set([5, 4, 3, 2, 1])
    #print(my_set[3]) # TypeError


def intersection():
    s1 = set([1, 2, 3, 4, 5])
    s2 = frozenset([4, 5, 6, 7, 8])
    s3 = s1 & s2
    print(s3) # set([4, 5])


if __name__ == "__main__":
    #no_indexing()
    intersection()