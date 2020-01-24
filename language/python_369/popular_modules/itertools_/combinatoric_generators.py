# https://docs.python.org/3.7/library/itertools.html#module-itertools


import itertools


def calculate_combinations_without_replacement(iterable, taken):
    # 4 letters taken 3 at a time without replacement, unordered
    print([''.join(x) for x in itertools.combinations(iterable, taken)]) # ['ABC', 'ABD', 'ACD', 'BCD']


if __name__ == '__main__':
    calculate_combinations_without_replacement('ABCD', 3)