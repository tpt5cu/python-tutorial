# https://docs.python-guide.org/writing/gotchas/#mutable-default-arguments


import tempfile, random


def modify_mutable_list():
    """
    Default parameters are evaluated exactly 1 time: when a function is created. Thus, the same mutable default parameter could be used for every call
    to a function. This will only happen if the mutable default parameter is used. If an argument is supplied which negates the usage of the default
    parameter, then that mutable parameter wouldn't be used at all.
    """
    def append_to_list(val, my_list=[]):
        my_list.append(val)
        return my_list

    l = append_to_list(5)
    print(l) # [5]
    l = append_to_list(10)
    print(l) # [5, 10]
    l2 = append_to_list('dog', [])
    print(l2) # ['dog']
    print(l) # [5, 10]


def modify_mutable_dict():
    '''
    Never ever use a dictionary as a default parameter. Why? Because if somebody modifies the dict, they could modify the dict for subsequent
    invocations of the same function.
    - Even if I don't modify the dict in the function, somebody in the future might and this will introduce a weird bug
    '''
    def mutable_dict(params={'count': 5, 'limit': 100, 'endpoint': 'last'}, modify=False):
        if modify:
            params['random'] = random.randint(-100, 0)
        print('params is: {}'.format(params))
    
    mutable_dict() # params is: {'count': 5, 'endpoint': 'last', 'limit': 100}
    mutable_dict(modify=True) # params is: {'count': 5, 'random': -12, 'endpoint': 'last', 'limit': 100}
    # This invocation is not okay because the default argument is not what the user expects
    mutable_dict() # params is: {'count': 5, 'random': -12, 'endpoint': 'last', 'limit': 100}
    # This invocation is okay because a new dict was passed
    mutable_dict(params={'hello': 'world'}) # params is: {'hello': 'world'}
    mutable_dict() # params is: {'count': 5, 'random': -12, 'endpoint': 'last', 'limit': 100}


def examine_function_calls():
    '''
    It's no surpise that if a default parameter is set to a function call, that function executes exactly once and every subsequent invocation of that
    function will have the default parameter set to the same value
    '''
    def function_call(dir=tempfile.mkdtemp()):
        print('Made new directory: {}'.format(dir))

    print(function_call() == function_call()) # True


if __name__ == "__main__":
    modify_mutable_list()
    #examine_function_calls()
    #modify_mutable_dict()