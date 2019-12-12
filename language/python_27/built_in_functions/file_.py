# https://docs.python.org/2.7/library/functions.html#file


def create_file_object():
    '''
    The file() built-in is its own distinct type
    - The parameters of file() are the same as those of open()
    '''
    f = file(__file__)
    print(type(f)) # <type 'file'>
    f.close()


if __name__ == '__main__':
    create_file_object()