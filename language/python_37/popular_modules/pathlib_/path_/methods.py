# https://docs.python.org/3.7/library/pathlib.html#methods


from pathlib import Path


'''There's a LOT of good stuff here like automatically opened and closed files'''


def file_object_exists():
    '''exists() doesn't care if the object is a file or directory, but the more specific variations do exist'''
    p = Path(__file__)
    print(p.exists()) # True
    p = Path('/Users/austinchang/tutorials/python/language/python_37/popular_modules/pathlib_/path_')
    print(p.exists()) # True


def get_matching_files():
    '''
    In order for glob() to work, the Path object must be a directory as opposed to a file    
    - glob() returns an iterator over Path objects that correspond to matching files, or an empty list
    - The glob pattern cannot be absolute
    - Recursive globbing is allowed
    '''
    p = Path(__file__)
    print(p.parent) # Depends on invocation

    # [PosixPath('/Users/austinchang/tutorials/python/language/python_37/popular_modules/pathlib_/path_/create.py'),
    # PosixPath('/Users/austinchang/tutorials/python/language/python_37/popular_modules/pathlib_/path_/methods.py')]
    print(list(p.parent.glob('*.py')))

    # [PosixPath('/Users/austinchang/tutorials/python/language/python_37/popular_modules/pathlib_/path_/create.py'),
    # PosixPath('/Users/austinchang/tutorials/python/language/python_37/popular_modules/pathlib_/path_/methods.py'),
    # PosixPath('/Users/austinchang/tutorials/python/language/python_37/popular_modules/pathlib_/purepath_/create.py'),
    # PosixPath('/Users/austinchang/tutorials/python/language/python_37/popular_modules/pathlib_/purepath_/methods.r2d2.py')]
    print(list(p.parent.parent.parent.glob('*/*/*.py')))

    print(list(p.parent.parent.parent.glob('*/*.py'))) # [PosixPath('/Users/austinchang/tutorials/python/language/python_37/popular_modules/csv_/writer_.py')]

    print(list(p.parent.parent.parent.glob('*[s_].py'))) # []

    # Do recursive globbing
    # [PosixPath('/Users/austinchang/tutorials/python/language/python_37/popular_modules/pathlib_/path_/methods.py'),
    # PosixPath('/Users/austinchang/tutorials/python/language/python_37/popular_modules/csv_/writer_.py')]
    print(list(p.parent.parent.parent.glob('**/*[s_].py')))


if __name__ == '__main__':
    #file_object_exists()
    get_matching_files()