'''
- In Python 2, map() returns a list where every item had <function> applied to it
- In Python 3, map() returns an iterator that WILL apply <function> to every item in <iterable>. THIS IS IMPORTANT FOR MATPLOTLIB.
'''


import inspect


def divide_list_elements():
    '''Notice how a list isn't printed anymore'''
    my_list = [2, 4, 6, 8, 10, 12]
    divided = map(lambda x: x / 2, my_list)
    print(type(divided)) # <class 'map'>
    print(inspect.getmro(divided.__class__))
    print(divided) # <map object at ...>
    #print(divided[0]) # TypeError: 'map' object is not subscriptable
    for i in divided:
        print(i) # 1.0\n2.0\n3.0\n4.0\n5.0\n6.0


if __name__ == "__main__":
    divide_list_elements()