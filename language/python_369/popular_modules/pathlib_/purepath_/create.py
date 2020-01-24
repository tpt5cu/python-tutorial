# https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f
# https://docs.python.org/3.7/library/pathlib.html


from pathlib import PurePath


'''
- Python can correctly translate a hard-coded path that uses "/" on Windows inside of an open() call
    - Don't rely on this behavior
    - Using backslashes on macOS will totally fail
- The old solution was to use os.path.join(), but it's very annoying
- Python 3 introduced pathlib to deal with this issue, and it's much better
    - In a nutshell, pathlib combines functionality from os and os.path into a single module with a better API, and adds more functionality

Recall that the value of __file__ depends on whether or not Python was run with -m. In any case, don't rely on it
- If it wasn't __file__ can change
- If it was, __file__ is absolute
'''


'''
Paths (PurePaths and concrete Paths) are 
- Immutable and therefore hashable
- Same flavor (i.e. all Posix or all Windows) paths are comparable and therefore orderable
    - Different flavor paths are not comparable and never equal

All Purepath and Path objects inherit the os.PathLike mixin and can be used as such
'''


def create_purepath():
    '''
    Instantiating a PurePath creates a concrete PurePosixPath or PureWindowsPath depending on the underlying OS
    - I'll almost never be using a PurePath in a string operation because 1) I can do just about any pathing operation with only PurePath objects 2)
      any operations that actually interact with the file system are handled by concrete Path objects
    - An empty initialization assumes the cwd
    '''
    pp = PurePath(__file__)
    print(type(pp)) # <class 'pathlib.PurePosixPath'>
    print(pp) # /Users/austinchang/tutorials/python/language/python_37/popular_modules/pathlib_/pure_paths.py
    print(str(pp)) # /Users/austinchang/tutorials/python/language/python_37/popular_modules/pathlib_/pure_paths.py
    print(repr(pp)) # PurePosixPath('/Users/austinchang/tutorials/python/language/python_37/popular_modules/pathlib_/pure_paths.py')
    pp = PurePath('~', '.bash_profile')
    print(pp) # ~/.bash_profile
    pp = PurePath(pathlib.Path('foo'), PurePath('bar'))
    print(pp) # foo/bar
    pp = PurePath()
    print(pp) # .
    # This doesn't belong here since it's a Path object, but it shows that "." really does correspond to the directory from which $ python $ was run
    print(pathlib.Path().resolve()) # /Users/austinchang/tutorials/python/language


def create_absolute_path():
    '''PurePath() copies the behavior of os.path() when it comes to creating absolute paths'''
    pp = PurePath('/foo', '/bar', '/baz', 'biz')
    print(pp) # /baz/biz


def collapse_extra_components():
    '''Remember that ".." in "foo/../bar" is not an extra component if the case where foo is a symbolic link to somewhere else is considered'''
    pp = PurePath('foo/./bar///baz/../biz')
    print(pp) # foo/bar/baz/../biz


def overload_slash_operator():
    '''The forward slash operator is overloaded so that it directly concatenates path components. Amazing'''
    pp = PurePath('/etc')
    pp = pp / 'users' / 'foobar' / '132^'
    print(pp) # /etc/users/foobar/132^


if __name__ == '__main__':
    #create_purepath()
    #create_absolute_path()
    #collapse_extra_components()
    overload_slash_operator()