"""
https://stackoverflow.com/questions/11502268/how-does-pythons-comma-operator-works-during-assignment
"""

"""
Normally, I see the "," character in lists, tuples, dictionaries, sets, etc. In those contexts, it's just a normal comma. 
"""

def sequence_unpack():
    """ Commas on the left-hand side indicate that values should be unpacked from a sequence """
    my_list = [1, 2, 3, 4, 5]
    a, b, c, d, e = my_list
    print(e)
    a, b = "HI"
    print(b)

def make_tuple():
    """ Commas on the right-hand side indicate that the right-hand value is a tuple """
    thing = 1, 2, 3, 4
    print(type(thing))

if __name__ == "__main__":
    #sequence_unpack()
    make_tuple()
