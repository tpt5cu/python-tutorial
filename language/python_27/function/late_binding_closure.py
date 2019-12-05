# https://docs.python-guide.org/writing/gotchas/#late-binding-closures


def create_multipliers():
    '''Get a list of 5 elements, where each element is its own function'''
    multipliers = []
    for i in range(5):
        def multiplier(x):
            return i * x
        multipliers.append(multiplier)
    return multipliers


def examine_bound_functions():
    '''
    Python's closures are LATE BINDING. That means the value of a variable that is used in a closure is looked up at RUN-TIME when the function that
    used a closure is called.
    - In this case 'i' goes from 0 to 4. When the functions in the list are invoked, 4 * 3 is performed inside each individual function.
    - It's the same for a lambda, as expected
    '''
    funcs = create_multipliers()
    for m in funcs:
        print(m(3)) # 12, 12, 12, 12, 12

    def create_lambda_multipliers():
        return [lambda x : i * x for i in range(5)]
    funcs = create_lambda_multipliers()
    for m in funcs: # 8, 8, 8, 8, 8
        print(m(2))


def correct_behavior():
    '''
    If I want to fake 'early binding' closures, I can exploit the behavior of default parameters. Since function parameters are new, declared local
    variables that are created along with a new function object, they are not affected by a closure.
    - I could also return a generator instead of a list
    '''
    def create_lambda_multipliers():
        #return [lambda x, i=i: x * i for i in range(5)] # returns a list
        return (lambda x: x * i for i in range(5)) # returns a generator
    funcs = create_lambda_multipliers()
    #print(type(funcs))
    for m in funcs:
        print(m(2)) # 0, 2, 4, 6, 8


if __name__ == '__main__':
    #examine_bound_functions()
    correct_behavior()