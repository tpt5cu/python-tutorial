# https://docs.python.org/3.8/reference/simple_stmts.html#grammar-token-nonlocal-stmt
# https://stackoverflow.com/questions/1261875/python-nonlocal-statement


'''The nonlocal statement was introduced in Python 3.0'''


my_var = 'global my_var'


def multiple_variables():
    x = 5
    y = 6
    def inner():
        nonlocal x, y
        x = -1
        y = -2
        print() # template strings, also comma assignment?


def examine_nonlocal():
    '''
    The "nonlocal" statement works like the "global" statement. It allows me to grab a variable from the immediately enclosing scope and assign it a value
    - The nonlocal statement cannot reference the global scope. That ability is reserved for the "global" statement
        - I cannot cheat to get around this either by trying to pass a variable through a global statement to a nonlocal statement
    - A variable cannot be assigned when preceeded by a nonlocal statement. The variable is already getting its value from the surrounding scope!
    - Consecutive nonlocal statements move the same outermost variable through all of the inner scopes, as expected
    '''
    #nonlocal my_var # SyntaxError
    # Valid, but breaks the inner nonlocal statements
    #global my_var 
    my_var = 'outer my_var'
    def middle():
        nonlocal my_var
        my_var = 'middle my_var'
        def inner():
            nonlocal my_var
            my_var = 'inner my_var'
            print('first: ' + my_var)  # inner my_var
        inner()
        print('second: ' + my_var) # inner my_var
    middle()
    print('third: ' + my_var) # inner my_var


if __name__ == '__main__':
    examine_nonlocal()
    print('last: ' + my_var) # global my_var