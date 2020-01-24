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
    dict_to_list()