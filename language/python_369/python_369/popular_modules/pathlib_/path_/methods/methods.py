# https://docs.python.org/3.6/library/pathlib.html#methods


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


def get_absolute_path():
    '''
    <Path>.resolve() does NOT return a string, but it DOES make sure that when the Path is converted into a string, that string is an absolute path
    - Just use str() to get a string
    '''
    p = Path(__file__)
    print(type(p)) # <class 'pathlib.PosixPath'>
    print(p) # methods.py, path_/methods.py, etc.
    print(str(p)) # methods.py, path_/methods.py, etc.
    abs_p = p.resolve()
    print(type(abs_p)) # <class 'pathlib.PosixPath'>
    print(abs_p) # /Users/austinchang/tutorials/python/language/python_37/popular_modules/pathlib_/path_/methods.py 
    print(str(abs_p)) # /Users/austinchang/tutorials/python/language/python_369/python_369/popular_modules/pathlib_/path_/methods/methods.py


def get_absolute_path2():
    # Redo the above example for the case of ~
    p = Path('~')
    # This is NOT what I want
    print(p.resolve()) # /Users/austinchang/tutorials/python/language/~


def read_and_write():
    '''A pathlib.Path object can read/write bytes and strs by itself'''
    print((Path(__file__).parent / 'src.txt').read_text()) # This is some source text data
    print((Path(__file__).parent / 'src.txt').read_bytes()) # b'This is some source text data'
    #(Path(__file__).parent / 'dst.txt').write_text('Hello there')
    (Path(__file__).parent / 'dst.txt').write_bytes(b'Hello there! G\xFFeneral Kenobi, you are a bold one.')


if __name__ == '__main__':
    #file_object_exists()
    #get_matching_files()
    #get_absolute_path()
    get_absolute_path2()
    #read_and_write()
