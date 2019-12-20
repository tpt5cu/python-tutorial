def find_():
    '''find() returns the index of the substring, or -1 if it isn't found'''
    string = 'Hi there'
    print(string.find('z')) # -1


def equals():
    '''Just use == to compare strings'''
    my_str = 'hello there'
    print(my_str == 'hello there\n') # False
    print(my_str.startswith('hello there\n')) # False
    print(my_str.startswith('hello there')) # True
    print(my_str == 'hello there') # True


def check_beginning_and_end():
    '''startswith() and endswith() are neat convenience methods'''
    string = 'I think that coconuts are cool.'
    print(string.startswith('I t')) # True
    print(string.endswith('cool')) # False


if __name__ == '__main__':
    find_()
    equals()
    check_beginning_and_end()