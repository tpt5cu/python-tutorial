"""
https://docs.python.org/2.7/tutorial/datastructures.html
"""

def py_append():
    """ list.append() adds an element to the end of the list in-place.
    """
    list = [1, 2, 3];
    list.append(4)
    print(list)

if __name__ == "__main__":
    py_append()