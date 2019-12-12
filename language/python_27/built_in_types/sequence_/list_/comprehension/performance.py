# https://portingguide.readthedocs.io/en/latest/iterators.htmo
# https://stackoverflow.com/questions/1247486/list-comprehension-vs-map - gory details


import timeit


numbers = [1, 2, 3, 4, 5, 6, 7]
powers_of_two_map = map(lambda x: 2**x, numbers)
powers_of_two_comp = [2**x for x in numbers]


'''
The results are surprising: using functions is faster than using list comprehensions in Python 3 while the opposite it true for Python 2
- Use comprehensions because they are more readable
'''


def use_functions():
    for number in filter(lambda x: x < 20, powers_of_two_map):
        #print(number) # 2\n4\n8\n16
        number += 1


def use_list_comprehensions():
    for number in [x for x in powers_of_two_comp if x < 20]:
        #print(number) # 2\n4\n8\n16
        number += 1


def time_function_usage():
    '''
    - Python 2: 1.65262982845
    - Python 3: 0.4861466310999999
    '''
    print(sum(timeit.repeat(
        setup='from __main__ import powers_of_two_map, use_functions;',
        stmt='use_functions()',
        repeat=10
    ))/10)


def time_list_comprehension_usage():
    '''
    - Python 2: 0.772179818153
    - Python 3: 1.2467536622000002
    '''
    print(sum(timeit.repeat(
        setup='from __main__ import powers_of_two_comp, use_list_comprehensions;',
        stmt='use_list_comprehensions()',
        repeat=10
    ))/10)


if __name__ == '__main__':
    #time_function_usage()
    time_list_comprehension_usage()