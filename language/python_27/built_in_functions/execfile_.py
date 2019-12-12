# https://docs.python.org/2.7/library/functions.html#execfile


import os


def execute_file():
    '''This function is just like exec() except it reads and executes a file'''
    print('Hello from execute file')
    p = os.path.join(os.path.dirname(__file__), 'enumerate_.py')
    execfile(p)


if __name__ == '__main__':
    execute_file()