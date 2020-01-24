# https://docs.python.org/3.8/library/functions.html#exec
# https://stackoverflow.com/questions/15086040/behavior-of-exec-function-in-python-2-and-python-3


'''The effect of exec() on the scope of variable in function is totally different in Python 3 from what it is in Python 2, and I don't completely understand why'''


global_var = 'global_var'


def modify_globals():
    '''globals() still reflects in both directions'''
    globals()['foo'] = 'bar'


def modify_variables_in_function_scope():
    # Nothing changes
    local_var = 'local_var'
    exec('local_var = 1; global_var = 2'); print(local_var, global_var) # local_var y
    # Nothing outside of the provided dictionary namespace changes
    namespace = {}; exec('local_var = 4; global_var = 5', namespace); print(namespace['local_var'], namespace['global_var'], local_var, global_var) # 4 5 local_var y
    # - local_var doesn't change (it cannot be changed in Python 3)
    # - global_var changes (this is different from Python 2)
    exec('local_var = 4; global_var = 5', globals()); print(local_var, global_var) # local_var 5
    # Nothing changes. I would expect global_var to change but it doesn't (This is different from Python 2)
    exec('local_var = 7; global_var = 8', globals(), locals()); print(local_var, global_var) # local_var 5


exec('local_var = "x"; global_var = "y"'); print(local_var, global_var) # x y


if __name__ == '__main__':
    modify_variables_in_function_scope()
    modify_globals(); print(foo) # bar