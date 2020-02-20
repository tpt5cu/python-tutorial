# https://docs.python.org/3.7/library/pathlib.html#accessing-individual-parts


from pathlib import PurePath


def access_components():
    '''<PurePath>.parts is an attribute that returns a tuple. Just about all of the other attributes are syntactic sugar on this tuple'''
    pp = PurePath(__file__)
    print(pp.parts) # ('/', 'Users', 'austinchang', 'tutorials', 'python', 'language', 'python_369', 'python_369', 'popular_modules', 'pathlib_', 'purepath_', 'attributes.py')
    

def access_filename():
    pp = PurePath(__file__)
    print(pp.name) # attributes.py


def access_root():
    '''Return the root of the path (empty string if it's a relative path'''
    pp = PurePath('foo/bar/baz')
    r = pp.root
    print(type(r)) # <class 'str'>
    print(r) # ''


def access_dirname_or_parent():
    '''
    The parent and dirname are one and the same for a file
    - The parent attribute is subject to the same limitations as os.path.dirname() when used with __file__
    '''
    pp = PurePath(__file__)
    print(type(pp.parent)) # <class 'pathlib.PurePosixPath'>
    # - /Users/austinchang/tutorials/python/language/python_37/popular_modules/pathlib_/purepath_
    # - Could also be "." or something else
    print(pp.parent) 


if __name__ == '__main__':
    #access_components()
    #access_filename()
    #access_root()
    access_dirname_or_parent()
