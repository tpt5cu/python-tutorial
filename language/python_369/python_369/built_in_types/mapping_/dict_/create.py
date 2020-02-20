def merge_dicts():
    '''
    This syntax is new in Python 3
    - The dictionary that is unpacked last gets precedence
    '''
    d2 = {'weather': 'sunny', 'color': 'purple'}
    d1 = {'direction': 'right', 'color': 'maroon'}
    d3 = {**d1, **d2}
    print(d3) # {'direction': 'right', 'color': 'purple', 'weather': 'sunny'}


if __name__ == '__main__':
    merge_dicts()