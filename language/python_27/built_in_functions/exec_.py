# https://docs.python.org/2.7/reference/simple_stmts.html#the-exec-statement
# https://stackoverflow.com/questions/15086040/behavior-of-exec-function-in-python-2-and-python-3


'''locals() only ever reflects variables in one direction in Python 2 and 3. Thus, modifying locals() won't actually modify the local namespace'''


global_var = 'global_var'


def modify_globals():
    '''globals() reflects in both directions'''
    globals()['foo'] = 'bar'


def modify_variables_in_function_scope():
    # If the optional arguments are omitted, the code is executed in the current scope
    # - Both local variables and global variables change
    local_var = 'local_var'
    exec('local_var = 1; global_var = 2'); print(local_var, global_var) # (1, 2)
    # If only one optional argument is given, it should be a dict exactly. It will hold global and local variables.
    # - Nothing outside of the provided dictionary namespace changes
    namespace = {}; exec('local_var = 4; global_var = 5', namespace); print(namespace['local_var'], namespace['global_var'], local_var, global_var) # (4, 5, 1, 2)
    # If globals() is provided instead of a dict, the global namespace still doesn't change
    exec('local_var = 4; global_var = 5', globals()); print(local_var, global_var) # (1, 2)
    # If both optional arguments are given, then the global namespace CAN be changed if globals() is provided
    exec('local_var = 7; global_var = 8', globals(), locals()); print(local_var, global_var) # (1, 8)


exec('local_var = "x"; global_var = "y"'); print(local_var, global_var) # ('x', 'y')


if __name__ == '__main__':
    modify_variables_in_function_scope()
    modify_globals(); print(foo) # bar