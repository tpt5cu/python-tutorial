# https://docs.python.org/3.7/library/pathlib.html#methods-and-properties - I don't want to list them all here


from pathlib import PurePath


def convert_to_uri():
    '''Put it in a web browser!'''
    pp = PurePath(__file__)
    print(pp.as_uri()) # file:///Users/austinchang/tutorials/python/language/python_37/popular_modules/pathlib_/purepath/methods.r2d2.py


def is_absolute():
    '''What about is_relative()? It's relative if it's not absolute!'''
    pp = PurePath(__file__)
    print(pp) # Depends on invocation
    print(pp.is_absolute()) # Depends on invocation


def join_path():
    '''
    Use the '/' syntax when convenient, otherwise use this
    - Remember that all PurePath and Path objects are immutable
    - Remember the behavior of joining absolute path components
    '''
    pp = PurePath('foobar')
    new_pp = pp.joinpath('baz', '/', 'zigzam')
    print(pp) # foobar
    print(new_pp) # /zigzam


def match_path_against_glob():
    # If <pattern> is relative, <PurePath> can be absolute or relative. Matching is done from the right
    relative = PurePath('foo/bar/baz/biz.py')
    print(relative.match('*.py')) # True

    relative = PurePath('business/as/usual/whoo.txt')
    print(relative.match('business/*')) # False
    print(relative.match('business/*/*')) # False
    print(relative.match('business/*/*/*yt')) # False
    print(relative.match('business/*/*/*t')) # True

    # If <pattern> is absolute, <PurePath> must be absolute and the entire path must match
    abs_ = PurePath('/Users/austinchang')
    print(abs_.match('*.ang')) # False
    print(abs_.match('/*/*ang')) # True
    print(abs_.match('/*')) # False


def get_relative_path():
    '''
    The provided argument must have the same root (whether relative or absolute) as the PurePath object
    - Example:
        - Original PurePath: <old>/<path>/<components>/<foo>
        - Argument: <old>/<path>
        - New, shorter Purepath: <components>/<foo>
    '''
    relative = PurePath('austinchang/tutorials/python/language/python_37/popular_modules/pathlib_/purepath/methods.r2d2.py')
    #print(relative.relative_to('python_37')) # ValueError
    print(relative.relative_to('austinchang/tutorials/python/language/python_37')) # popular_modules/pathlib_/purepath/methods.r2d2.py


def replace_filename():
    '''I can only replace the filename. Fails on PurePaths that never had a filename to begin with'''
    relative = PurePath('austinchang/tutorials/python/language/python_37/popular_modules/pathlib_/purepath/methods.r2d2.py')
    print(relative.with_name('davidchang')) # austinchang/tutorials/python/language/python_37/popular_modules/pathlib_/purepath/davidchang
    abs_ = PurePath('/')
    print(abs_.with_name('hi')) # ValueError: PurePosixPath('/') has an empty name


def replace_suffix():
    '''
    Only the last suffix (I guess that's the only suffix, technically) can be replaced
    - A suffix can be added to anything
    '''
    relative = PurePath('austinchang/tutorials/python/language/python_37/popular_modules/pathlib_/purepath/methods.r2d2.py')
    print(relative.with_suffix('.js')) # austinchang/tutorials/python/language/python_37/popular_modules/pathlib_/purepath/methods.r2d2.js
    no_suffix = PurePath('/foobar/')
    print(no_suffix.with_suffix('.dope')) # /foobar.dope
    removed_suffix = PurePath('help.js')
    print(removed_suffix.with_suffix('')) # help


def get_absolute_path():
    '''See pathlib.Path'''
    pass


if __name__ == '__main__':
    #access_components()
    #access_root()
    access_dirname_or_parent()
    #access_filename_variations()
    #convert_to_uri()
    #is_absolute()
    #join_path()
    #match_path_against_glob()
    #get_relative_path()
    #replace_filename()
    #replace_suffix()