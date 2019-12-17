def open_nonexistent_file():
    '''Attempting to open a nonexistent file/directory will raise an IOError with errno == 2'''
    with open('./blahblah') as f:
        text = f.read()


def catch_exception():
    '''
    If some other process were to delete a file in between my validation that the file existed and my attempt to access it, I would want to catch that
    exception.
    '''
    try:
        # Pretend this file existed just before this line
        with open('./blahblah') as f:
            text = f.read()
    except IOError as e:
        if e.errno == 2:
            print('Tried to open a nonexistent file. Proceed as normal')


if __name__ == '__main__':
    #open_nonexistent_file()
    catch_exception()