# https://docs.python.org/3/library/stdtypes.html#mapping-types-dict - dict documentation


def merge_dicts():
    '''
    This syntax is new in Python 3
    - The dictionary that is unpacked last gets precedence
    '''
    d2 = {'weather': 'sunny', 'color': 'purple'}
    d1 = {'direction': 'right', 'color': 'maroon'}
    d3 = {**d1, **d2}
    print(d3) # {'direction': 'right', 'color': 'purple', 'weather': 'sunny'}


def create_empty_dict():
    '''
    Do this when I want to create a dict with known keys but I don't have any values. Using the classmethod dict.fromkeys() is the most idiomatic way
    of doing this
    '''
    keys = ['foo', 'bar', 'baz', 'boo']
    d = dict.fromkeys(keys, None)
    print(d)


if __name__ == '__main__':
    #merge_dicts()
    create_empty_dict()
