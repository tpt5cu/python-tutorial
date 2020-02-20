from module_.import_.awesome_module import awesome_function


'''
Python does not have function hoisting per se, but when a Python file is parsed from top to bottom, a new function definition later on
will shadow an earlier defined function definition
'''


# def awesome_function() hasn't been reached yet, so the imported function is used
# - If there is no import, than this is a NameError
awesome_function() # I'm an awesome function


def do_stuff():
    awesome_function()


def awesome_function():
    print("I'm a terrible function")


if __name__ == '__main__':
    # def awesome_function has been reached last, so it takes precedence
    do_stuff() # I'm a terrible function