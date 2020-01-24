# https://renzo.lucioni.xyz/pythons-set-literals/


def set_literal():
    '''
    Set literals are more efficient than the set constructor because the set constructor requires that I create another iterable to pass into the set
    constructor
    '''
    set_ = {8, 1, -44}
    print(type(set_)) # <class 'set'>


if __name__ == '__main__':
    set_literal()