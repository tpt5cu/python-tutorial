# https://docs.python.org/2/library/functions.html#zip


'''zip() now return an iterator'''


def combine_lists():
    a = [1, 2, 3]
    b = [4, 5, 6, 7]
    c = zip(a, b)
    print(type(c)) # <class 'zip'>
    print(c) # <zip object at ...>
    print(list(c)) # [(1, 4), (2, 5), (3, 6)]


def unpack_zip():
    '''Yes, a generator object can be unpacked into a function with the * syntax'''
    def consume_tuple(x, y):
        print('x: {}'.format(x)) # x: (1, 'a')
        print('y: {}'.format(y)) # y: (2, 'b')
    list_1 = [1, 2]
    list_2 = ['a', 'b']
    gen = zip(list_1, list_2)
    consume_tuple(*gen)



if __name__ == '__main__':
    #combine_lists()
    unpack_zip()