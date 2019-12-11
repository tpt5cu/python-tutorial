"""
https://pythontips.com/2013/08/02/what-is-pickle-in-python/
https://stackoverflow.com/questions/18474791/decreasing-the-size-of-cpickle-objects
"""

import pickle, os, gzip, random

"""
The pickle module is for serializing and deserializing Python objects. Any Python object can be pickled so that it can be saved on the disk. The
action of "pickling" is converting a Python object into a character stream with the necessary data so that the object can be reconstructed in another
Python script.

The most common file extension for a Python pickle file is ".pkl" for Python2 and ".pickle" for Python3
"""


filename = os.path.join(os.path.dirname(__file__), "delicious-pickle.pkl") 
new_filename = filename.split(".")[0] + ".pkl.gz"


def get_2d_matrix():
    words = ["Returns", "a", "new", "list", "containing", "elements", "from", "the", "population", "while", "leaving", "the", "original", "population", "unchanged.", "The", "resulting", "list", "is", "in", "selection", "order", "so", "that", "all", "sub-slices", "will", "also", "be", "valid", "random", "samples.", "This", "allows", "raffle", "winners", "(the", "sample)", "to", "be", "partitioned", "into", "grand", "prize", "and", "second", "place", "winners", "(the", "subslices)."]
    matrix = []
    for x in range(100):
        my_list = []
        if x % 2 == 0:
            for y in range(100):
                my_list.append(random.randint(0, 100))
        else:
            for y in range(100):
                my_list.append(random.choice(words))
        matrix.append(my_list)
    return matrix


def pickle_dump():
    """ A Python object can be written to a file with the dump() method. """
    with open(filename, 'w') as f:
        pickle.dump(get_2d_matrix(), f) # file size is 50 KB


def pickle_load():
    """ A Python object can be loaded from a file into memory with the load() method. """
    with open(filename) as f:
        data = pickle.load(f)
    print(data)


def pickle_dump_compression():
    """
    Compression isn't built-in to the pickle module, but pickle files are so large that it is very common to compress them. Simply create a gzip file
    (or use some other compression format/algorithm) and write the serialized object to that file.
    """
    with gzip.GzipFile(new_filename, 'w') as f:
        pickle.dump(get_2d_matrix(), f) # file size is 13 KB


def pickle_load_compression():
    """ Again, compression isn't built-in so I have to know the compression format to open the compressed file. """
    with gzip.GzipFile(new_filename) as f:
        data = pickle.load(f)
    print(data)



if __name__ == "__main__":
    #pickle_dump()
    #pickle_load()
    #pickle_dump_compression()
    pickle_load_compression()