# https://docs.python-guide.org/writing/gotchas/#mutable-default-arguments


def append_to_list(val, my_list=[]):
    my_list.append(val)
    return my_list


def examine_mutable_default_parameter():
    """
    Default parameters are evaluated exactly 1 time: when a function is created. Thus, the same mutable default parameter could be used for every call
    to a function. This will only happen if the mutable default parameter is used. If an argument is supplied which negates the usage of the default
    parameter, then that mutable parameter wouldn't be used at all.
    """
    l = append_to_list(5)
    print(l) # [5]
    l = append_to_list(10)
    print(l) # [5, 10]
    l2 = append_to_list('dog', [])
    print(l2) # ['dog']
    print(l) # [5, 10]



if __name__ == "__main__":
    examine_mutable_default_parameter()