# https://docs.python.org/3.7/library/copy.html


import copy


def deep_copy():
    '''deepcopy works!'''
    names = ['Arne', 'Melissa', 'Dan']
    dicts_ = {'foo': 'bar', 'baz': 'boo'}
    compound = [names, dicts_]
    print(f'compound: {compound}')
    compound_copy = copy.deepcopy(compound)
    compound_copy[0][2] = 200
    compound_copy[1]['foo'] = 100
    print(f'compound: {compound}')
    print(f'compound_copy: {compound_copy}')


def circular_deep_copy():
    '''objects that reference themselves can also be copied'''
    dict_ = {'foo': 'bar'}
    dict_['foo'] = dict_
    print(f'dict_: {dict_}') # dict_: {'foo': {...}}
    print(f'dict_["foo"]: {dict_["foo"]}') # dict_["foo"]: {'foo': {...}}
    dict_copy = copy.deepcopy(dict_)
    print(f'dict_copy: {dict_copy}') # dict_copy: {'foo': {...}}
    print(f'dict_copy["foo"]: {dict_copy["foo"]}') # dict_copy["foo"]: {'foo': {...}}
    #print(dict_copy["foo"] == dict_["foo"]) # RecursionError
    #print(dict_copy == dict_) # RecursionError


def copy_function():
    '''As documented, if a function or class is deep-copied, the original object is returned unchanged'''
    func = deep_copy
    func_copy = copy.deepcopy(deep_copy)
    print(func is func_copy) # True


if __name__ == '__main__':
    #deep_copy()
    #circular_deep_copy()
    copy_function()