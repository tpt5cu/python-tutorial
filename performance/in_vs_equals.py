import sys
import random
import timeit
from performance.python_timeit import wrapper

target_strings = ["latitude", "longitude"]
random_strings = ["cat", "frog", "fatitude", "gross", "incredible", "bus", "serial", "voltage", "nominal", "possible", "longish", "lobby", "crash", "tonight", "wonderful", "amazing", "whoop", "latitude", "longitude"]
global_seed = 64
global_num = 10000


def compare_with_equals(num=global_num, seed=global_seed):
    count = 0
    random.seed(seed)
    for x in range(num):
        string = random.choice(random_strings)
        if string == "latitude" or string == "longitude":
            count += 1
    return count


def compare_with_in(num=global_num, seed=global_seed):
    count = 0
    random.seed(seed)
    for x in range(num):
        string = random.choice(random_strings)
        for subKey in ["latitude", "longitude"]:
            if subKey in string:
                count += 1
    return count


def compare_results():
    equals_count = compare_with_equals()
    in_count = compare_with_in()
    print(equals_count)
    print(in_count)


def time_functions():
    iterations = 1000
    equals_func = wrapper(compare_with_equals)
    in_func = wrapper(compare_with_in)
    print("Using equals operator: " + str(timeit.timeit(equals_func, number=iterations)))
    print("Using in operator: " + str(timeit.timeit(in_func, number=iterations)))


if __name__ == "__main__":
    """Okay this is crazy. 'in' is a littler slower than using ==. I guess the performance difference in the lat/lon
    parsing was due to an inefficient dictionary lookup which isn't cached very well?
    """
    print(sys.version)
    compare_results()
    time_functions()