from functools import reduce


def consume_iterable():
    '''
    - reduce() consumes a generator just fine
    - reduce() must take 2 arguments
    '''
    val = reduce(lambda reducer, a: reducer + a, map(lambda y: y + 1, [2, 3, 4]))
    # [2, 3, 4] -> [3, 4, 5] -> (((0 + 3) + 4) + 5) = 12
    print(val) # 12


if __name__ == '__main__':
    consume_iterable()