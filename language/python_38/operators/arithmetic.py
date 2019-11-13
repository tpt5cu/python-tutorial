def regular_division():
    '''
    Division with ints will always result in a float
    - I have to manually go through the OMF to make this change :'(
    '''
    print(5 / 4) # 1.25
    print(type(5 / 5)) # <class 'float'>


def floor_division():
    '''floor divison will always result in an int'''
    print(5 // 4) # 1
    print(type(5 // 5)) # <class 'int'>


if __name__ == '__main__':
    regular_division()
    floor_division()