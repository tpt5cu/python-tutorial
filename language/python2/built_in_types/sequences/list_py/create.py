def fixed_size_fixed_element():
    """
    I can create a list of a specific size with a specific element by multiplying the list. This is referred to as "repetition", since whatever
    elements in the sequence will be repeated x times
    """
    l = [0] * 10
    print(l) # a list filled with 10 0s


def multiple_fixed_size_fixed_element():
    """This is also an example of repetition"""
    l = [1, 2] * 10
    print(l) # 20 elements total, alternating 1 and 2


def fixed_size_non_integer_elements():
    """
    Doing this works just fine. That's because multipling a sequence by a scalar does not perform arithmetic multiplication, regardless of whether or
    not the elements of the sequence are integers. That's how repetition works.
    """
    l = ["A"] * 10
    print(l)
    print("A" * 10)


def concatenation():
    """The "+" operator performs concatenation for all sequence types."""
    l1 = ["a", "b", "c"]
    l2 = ["3", "2", "1"]
    l3 = l1 + l2
    print(l3)


def from_iterable():
    my_tup = (1, 2, 3)
    my_list = list(my_tup)
    print(my_list)


if __name__ == "__main__":
    #fixed_size_fixed_element()
    #multiple_fixed_size_fixed_element()
    #fixed_size_non_integer_elements()
    #concatenation()
    from_iterable()