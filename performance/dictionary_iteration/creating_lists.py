import random
import sys
import timeit
from performance.python_timeit import wrapper


def create_many_lists(my_dict):
    # type: (dict) -> int
    """Using <dictionary>.items() thousands of times is very SLOW because the function has the overhead of creating
    thousands of lists!
    """
    count = 0
    for key, val in my_dict.items():
        for sub_key, sub_val in val.items():
            if sub_key < 50:
                count += 1
    return count


def quick_iteration(my_dict):
    """This function isn't much faster than the slow one in Python 3.7. In Python 2.7, it slightly faster by
    a constant factor.
    """
    count = 0
    for key in my_dict:
        for sub_key in my_dict[key]:
            if sub_key < 50:
                count += 1
    return count


def get_huge_dictionary():
    """zip() returns an iterator of tuples. This iterator stops when the shortest iterable object is exhausted, so
    the iterator will only contain as many tuples as the shortest iterable that was passed. Remember, a dictionary
    key-value pair will be OVERWRITTEN if an existing key is assigned a value.
    """
    main_dict_size = 1000
    sub_dict_size = 100
    main_dict = {}
    for x in range(main_dict_size):
        num_list = []
        for y in range(sub_dict_size):
            num = random.random() * random.randint(0, 100)
            num_list.append(num)
        str_list = []
        for y in range(sub_dict_size):
            ltr = random.choice(["A", "B", "C", "D", "E", "F"])
            str_list.append(ltr)
        sub_dict = dict(zip(num_list, str_list))
        main_dict[x] = sub_dict
    #print("Main dictionary size: " + str(len(main_dict)))
    #print(main_dict)
    return main_dict


def time_iteration():
    my_dict = get_huge_dictionary()
    slow = wrapper(create_many_lists, my_dict)
    fast = wrapper(quick_iteration, my_dict)
    print("Slow: " + str(timeit.timeit(slow, number=1000)))
    print("Fast: " + str(timeit.timeit(fast, number=1000)))


def compare_results():
    my_dict = get_huge_dictionary()
    print("Slow iteration produced result of: " + str(create_many_lists(my_dict)))
    print("Fast iteration produced result of: " + str(quick_iteration(my_dict)))


if __name__ == "__main__":
    """Python 3.7:
    Slow: 14.93 seconds
    Fast: 14.26 seconds
    Python 2.7:
    Slow: 13.06
    Fast: 9.80
    
    My testing for this stuff was inspired by two parsing functions for .omd data. However, it appears
    the real slowdown is == vs 'in' operator, NOT creating lists from dictionaries.
    """
    print(sys.version)
    time_iteration()
    compare_results()


