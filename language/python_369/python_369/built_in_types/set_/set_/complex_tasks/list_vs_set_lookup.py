import timeit, random
from io_.open_.modes import get_permutations, get_all_permutations


p1 = get_permutations('r')
set_ = {*get_all_permutations()}
def validate_all_read_permutations_with_set():
    for p in p1:
        assert p in set_


p2 = get_permutations('r')
list_ = random.shuffle(get_all_permutations())
#list_ = get_all_permutations()
def validate_all_read_permutations_with_list():
    for p in p2:
        assert p in list_


def time_lookup_times():
    '''
    Python list lookup must be really optimized because usually the list lookup beats the set
    - This function was run 2 times, with comparable times listed in the same relative order. The list was shuffled for these runs
    - I can't even tell if shuffling the list makes any difference
    - Doesn't matter if I move the permutation inside of the function or not
    '''
    # 1.7854426322000005
    # 1.7917690103000001
    # 1.8049640079999996
    print(sum(timeit.repeat(
        setup='from __main__ import p1, set_, validate_all_read_permutations_with_set',
        #setup='from __main__ import validate_all_read_permutations_with_set',
        stmt='validate_all_read_permutations_with_set',
        number=100000000,
        repeat=10,
    ))/10)
    # 1.7559476496
    # 1.7604879587999989
    # 1.7427238400000011
    print(sum(timeit.repeat(
        setup='from __main__ import p2, list_, validate_all_read_permutations_with_list',
        #setup='from __main__ import validate_all_read_permutations_with_list',
        stmt='validate_all_read_permutations_with_list',
        number=100000000,
        repeat=10
    ))/10)


if __name__ == '__main__':
    time_lookup_times()