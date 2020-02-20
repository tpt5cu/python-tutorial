# https://docs.python.org/3.7/library/functools.html#functools.lru_cache
# https://stackoverflow.com/questions/49883177/how-does-lru-cache-from-functools-work


import timeit
from functools import lru_cache


'''
Possible options for caching the result(s) of a function
1) Have the function's result be stored in a global variable (ew)
    - This assumes that the function doesn't accept any arguments and thus cannot return different values. The function is explicitly a helper
      function that does a calculation and always returns the same value
2) Use @functools.lru_cache
    - A dictionary is used under the hood to store the results, so all args and kwargs must be hashable
    - If kwargs are in a different order, each gets a separate cache entry
    - set "maxsize" to None to let the cache grow unbounded
        - "maxsize" defaults to 128
        - Best performance of the LRU occurs when maxsize is a power of 2
    - set "typed" to True to give arguments with different types separate cache entries
'''


#@lru_cache()
def recursive_fibonacci(n):
    '''
    Calculate the nth fibonacci number
    - 0, 1, 1, 2, 3, 5, 8, 13, 21, etc. 
    - By definition, the first two fibonacci numbers are 0 and 1
    '''
    if n < 1:
        raise Exception
    if n < 3:
        return n - 1
    else:
        return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


def test_cache():
    # This call returns instantly when the lru_cache is used. Why? Because every recursive-call is cached!
    print(recursive_fibonacci(35)) # 5702887
    print(recursive_fibonacci.cache_info()) # CacheInfo(hits=32, misses=35, maxsize=128, currsize=35)
    print(timeit.timeit( # 0.130684091
        setup= 'from __main__ import recursive_fibonacci',
        stmt='recursive_fibonacci(35)',
    ))


#@lru_cache(maxsize=0) # This is dumb. But it's allowed!
@lru_cache(maxsize=1)
def fixed_recursive_fibonacci():
    return recursive_fibonacci(35)


def test_no_argument_cache():
    '''When a function has no parameters, its one and only result is cached successfully'''
    print(fixed_recursive_fibonacci()) # 5702887
    print(fixed_recursive_fibonacci()) # 5702887
    print(fixed_recursive_fibonacci()) # 5702887


if __name__ == '__main__':
    #print(recursive_fibonacci(4)) # 2
    #print(recursive_fibonacci(9)) # 21
    #test_cache()
    test_no_argument_cache()