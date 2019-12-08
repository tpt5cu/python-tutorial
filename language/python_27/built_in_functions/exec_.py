# https://docs.python.org/2.7/reference/simple_stmts.html#the-exec-statement
# https://stackoverflow.com/questions/15086040/behavior-of-exec-function-in-python-2-and-python-3


'''The exec statement was changed into a function in Python 3, but the function form work in Python 2.7 as well'''


def execute_string_code():
    '''
    Code is executed in the current scope, unless dictionaries are passed which specify the global and/or local variables to be 
    available in the scope
    - In Python 3, the actual surrounding scope CANNOT be modified by the exec function
    '''
    exec('x = 1 + 3')
    print(x) # 4


if __name__ == '__main__':
    execute_string_code()