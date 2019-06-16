

def fixed_size_fixed_element():
    """ I can create a list of a specific size with a specific element by multiplying the list """
    l = [0] * 10
    print(l) # a list filled with 10 0s


def multiple_fixed_size_fixed_element():
    l = [1, 2] * 10
    print(l) # 20 elements total, alternating 1 and 2


def fixed_size_non_integer_elements():
    """
    Doing this works just fine. That's because multipling a sequence by a scalar does not perform arithmetic multiplication, regardless of if the
    elements of the sequence are integers.
    """
    l = ["A"] * 10
    print(l)
    print("A" * 10)


if __name__ == "__main__":
    #fixed_size_fixed_element()
    #multiple_fixed_size_fixed_element()
    fixed_size_non_integer_elements()