# https://docs.python.org/2.7/howto/sorting.html#sort-stability-and-complex-sorts
# https://stackoverflow.com/questions/11476371/sort-by-multiple-keys-using-different-orderings
# https://stackoverflow.com/questions/20202418/why-is-the-cmp-parameter-removed-from-sort-sorted-in-python3-0


import timeit, functools
from built_in_functions.sorted_.introduction import custom_cmp_by_year_validcount_name, get_data, index_multisort


'''
The docs say that sorting with multiple keys, where the keys can have different ordering preferences, is done most efficiently with multiple sorting
passes because Python's internal Timsort algorithm uses any existing orderings in the dataset when it makes a sorting pass. 
- Supposedly, sorting with multiple passes is faster than using a cmp function (which was removed in Python 3 anyway) 
    - The timeit() results show this is not always true
'''


def sort_by_year_validlines_name_with_custom_cmp():
    '''
    Stable sorted:
        ['hourly', '2000', 'Alaska', 8760, 5000, 3760]
        ['hourly', '2000', 'Alabama', 8760, 4000, 4760]
        ['hourly', '2000', 'Virginia', 8760, 4000, 4760]
        ['hourly', '2000', 'Maine', 8760, 3000, 5760]
        ['hourly', '2001', 'Alaska', 8760, 5001, 3760]
        ['hourly', '2001', 'Alabama', 8760, 4001, 4760]
        ['hourly', '2001', 'Virginia', 8760, 4001, 4760]
        ['hourly', '2001', 'Maine', 8760, 2999, 5760]
    '''
    data = get_data()
    sorted_data = sorted(data, cmp=custom_cmp_by_year_validcount_name)
    for e in sorted_data:
        #print(e)
        pass
    return sorted_data


def sort_by_year_validlines_name_with_multiple_passes():
    '''
    - year is e[1], ascending
    - valid lines is e[4], descending
    - name is e[2], ascending
    '''
    data = get_data()
    sorted_data = index_multisort(data, ((1, False), (4, True), (2, False)))
    for e in sorted_data:
        #print(e)
        pass
    return sorted_data


def sort_by_year_validlines_name_with_custom_cmp_to_key():
    '''The function returned by functools.cmp_to_key() is extremeley slow for my use case'''
    data = get_data()
    sorted_data = sorted(data, key=functools.cmp_to_key(custom_cmp_by_year_validcount_name))
    for e in sorted_data:
        #print(e)
        pass
    return sorted_data


def compare_sorting_results():
    s1 = sort_by_year_validlines_name_with_multiple_passes()
    s2 = sort_by_year_validlines_name_with_custom_cmp()
    s3 = sort_by_year_validlines_name_with_custom_cmp_to_key()
    print(s1 == s2 == s3) # True


def compare_sorting_speeds():
    '''
    - I'm really surprised by this result. The custom 'cmp' function performs consistenly (but not ALWAYS) better than multiple sorting passes
    - Also, the function returned by cmp_to_key is incredibly slow. I can't even time it on the same scale as the other sorting approaches
    '''
    # Python 2:
    # - Time is 0.137748003006 for 10,000 cycles
    # - Time is 8.84350919724 for 1,000,000
    # Python 3: can't be done
    '''
    print(
        timeit.timeit(
            setup='from built_in_functions.sorted_.introduction import get_data; data = get_data(); from __main__ import sort_by_year_validlines_name_with_custom_cmp',
            stmt='sort_by_year_validlines_name_with_custom_cmp()',
            #number=10000
        )
    )
    '''
    # Python 2:
    # - Time is 0.171017169952 for 10,000 cycles
    # - Time is 10.3939599991 for 1,000,000 cycles
    # Python 3:
    # - Time is 0.147613463 for 10,000 cycles
    # - Time is 6.174809591000001 for 1,000,000 cycles
    '''
    print(
        timeit.timeit(
            setup='from built_in_functions.sorted_.introduction import get_data; data = get_data(); from __main__ import sort_by_year_validlines_name_with_multiple_passes',
            stmt='sort_by_year_validlines_name_with_multiple_passes()',
            number=10000
        )
    )
    '''
    # Python 2:
    # - Time is 1.06780982018 for 10,000 cycles
    # - Time is ? for 1,000,000 cycles (doesn't finish)
    # Python 3:
    # - Time is 0.139409987 for 10,000 cycles
    # - Time is 10.474761258 for 1,000,000 cycles
    print(
        timeit.timeit(
            setup='from built_in_functions.sorted_.introduction import get_data; data = get_data(); from __main__ import sort_by_year_validlines_name_with_custom_cmp_to_key',
            stmt='sort_by_year_validlines_name_with_custom_cmp_to_key()',
            number=10000
        )
    )


if __name__ == '__main__':
    #sort_by_year_validlines_name_with_custom_cmp()
    #sort_by_year_validlines_name_with_multiple_passes()
    #sort_by_year_validlines_name_with_custom_cmp_to_key()
    #compare_sorting_results()
    compare_sorting_speeds()