import random


# This line is run when the operations module is imported
#print("Hello from __init__.py")


def get_mixed_matrix():
    """ Return a 10 x 10 2d matrix that is a list of lists """
    words = ["Returns", "a", "new", "list", "containing", "elements", "from", "the", "population", "while", "leaving", "the", "original", "population", "unchanged.", "The", "resulting", "list", "is", "in", "selection", "order", "so", "that", "all", "sub-slices", "will", "also", "be", "valid", "random", "samples.", "This", "allows", "raffle", "winners", "(the", "sample)", "to", "be", "partitioned", "into", "grand", "prize", "and", "second", "place", "winners", "(the", "subslices)."]
    matrix = []
    for x in range(10):
        my_list = []
        if x % 2 == 0:
            for y in range(10):
                my_list.append(random.randint(0, 100))
        else:
            for y in range(10):
                my_list.append(random.choice(words))
        matrix.append(my_list)
    return matrix