# https://docs.python.org/3.6/library/inspect.html#module-inspect

import inspect

def get_module_filepath():
    '''The inspect module isn't necessary to find the file path of a module'''
    print(inspect.__file__)


if __name__ == '__main__':
    get_module_filepath()
