def repetition():
    '''
    When a list is multiplied by an int, what really happens is the repetition operator is used
    - The repetition operator creates a shallow copy of each element from the original list in the new list
    - It does not matter what order the operands are: if one of the operands is a list and one is an int, the * operator is always overloaded
        - If element-wise multiplication is happening, it's probably because one of the operands is an ndarray, not a Python list
    '''
    def repetition_func(_list, val):
        return _list * val
    x = [1, 2, 3]
    y = repetition_func(x, 3)
    print(x) # [1, 2, 3]
    print(y) # [1, 2, 3, 1, 2, 3, 1, 2, 3]

    def repetition_func2(_list, val):
        return val * _list
    x = [1.1, 'boo', 2]
    y = repetition_func2(x, 3)
    print(x) # [1.1, 'boo', 2]
    print(y) # [1.1, 'boo', 2, 1.1, 'boo', 2, 1.1, 'boo', 2]


def dict_to_list():
    '''
    - [<dict>.keys()] or [<dict>] is bad because it works AND it's almost never what I want
    - Instead, do list(<dict>)
    '''
    dict_ = {
        'foo': 'food',
        'bar': 'bard'
    }
    list_ = [dict_.keys()]
    print(type(list_)) # <class 'list'>
    print(len(list_)) # 1
    print(type(list_[0])) # <class 'dict_keys'>
    print(list_) # [dict_keys(['foo', 'bar'])]
    print(list_[0]) # dict_keys(['foo', 'bar'])
    print('')
    list_ = [dict_]
    print(type(list_)) # <class 'list'>
    print(len(list_)) # 1
    print(type(list_[0])) # <class 'dict'>
    print(list_) # [{'foo': 'food', 'bar': 'bard'}]
    print('')
    list_ = list(dict_.keys())
    print(list_) # ['foo', 'bar']


if __name__ == '__main__':
    repetition()
    #dict_to_list()
