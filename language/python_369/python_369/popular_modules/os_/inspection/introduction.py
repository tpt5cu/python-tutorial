import os


def get_cwd():
    '''There is no os.cwd attribute or os.cwd() method'''
    print(os.getcwd()) # /Users/austinchang/tutorials/python/language


if __name__ == '__main__':
    get_cwd()
