# https://docs.python.org/2/library/os.path.html


import os


def examine_paths():
    '''As long as I'm using os.path.abspath(), I will always get an absolute file path or an absolute directory path.'''
    print('__file__: ' + __file__) # this changes
    print('__file__ dirname: ' + os.path.dirname(__file__)) # this changes
    print('__file__ basename: ' + os.path.basename(__file__)) # does not change (it's the name of the file)
    absolute_path = os.path.abspath(__file__) # does not change
    print('absolute_path: ' + absolute_path)
    absolute_path_dir = os.path.dirname(os.path.abspath(__file__)) # does not change
    print('absolute_path dirname: ' + absolute_path_dir)
    absolute_path_basename = os.path.basename(os.path.abspath(__file__)) # does not change (it's the name of the file)
    print('absolute_path basename: ' + absolute_path_basename)


def resolve_relative_path():
    '''
    I should not use relative paths when opening files because the relative path will be resolved according to the cwd, which is set by where $ python
    $ is run. I should not use hard-coded absolute paths because then no other machine will be able to run my code. Instead, I should use the os.path
    module
    - This strategy works fine when Python's own open() function is being used to access a file. However, if I'm printing the joined path somewhere
      else like an HTML file, the absolute vs. relative value of __file__ matters. See the file_py.py notes. 
    '''
    # This is bad. I have to run $ python $ from /Users/austinchang/tutorials/python/language/python2 for this to work
    #with open('../../.gitignore') as f:
        #print(f.readlines())
    # This is bad
    #with open('/Users/austinchang/tutorials/python/.gitignore') as f:
        #print(f.read())
    # This is good. It will work anywhere. We go from /Users/austinchang/tutorials/python/language/python2/io_py to /Users/austinchang/tutorials/python
    # It does not matter that __file__ could be: language/python2/io_py/file_paths.py, or python2/io_py/file_paths.py, or io_py/file_paths.py, or
    # anything else
    file_path = os.path.join(os.path.dirname(__file__), '../../../.gitignore')
    print('file_path: ' + file_path)
    with open(file_path) as f:
        print(f.read())


def normalize_path():
    '''
    os.path.normpath removes redundant slashes and collapses relative separators (i.e '..'). It does not remove spaces or place a path with spaces in quotations.
    '''
    p = (os.path.join('hello/', 'my//', 'name///', 'is', '../Austin'))
    print(p) # hello/my//name///is/../Austin
    print(os.path.normpath(p)) # hello/my/name/Austin
    p = (os.path.join('this ', ' path ', '  has  ', 'spaces  '))
    print(p) # this / path /  has  /spaces
    print(os.path.normpath(p)) # this / path /  has  /spaces


def get_filename_with_extension():
    '''The filename with extension is also known as the basename of the file'''
    print(os.path.basename(__file__)) # file_paths.py


def get_filename_without_extension():
    print(os.path.basename(__file__).split('.')[0]) # file_paths


def get_last_path_component():
    '''os.path.split(<path>) returns (head, tail), where tail is the last part of the path without any slashes and head is everything before that.'''
    p = '/This/is/a/path/to/some/resources'
    head, tail = os.path.split(p)
    print(head) # /This/is/a/path/to/some
    print(tail) # resources
    head, tail = os.path.split(head)
    print(head) # /This/is/a/path/to
    print(tail) # some
    head, tail = os.path.split(tail)
    print(head) # ''
    print(tail) # some
    head, tail = os.path.split('/')
    print(head) # /
    print(tail) # ''


def join_with_empty_string():
    '''When a path is joined with an empty string, the result is a directory entry (i.e. a path with a trailing slash)'''
    filenames = [os.path.join('hello', 'world', filename) for filename in 'yes', 'no', '']
    print(filenames) # ['hello/world/yes', 'hello/world/no', 'hello/world/']
    print(os.path.join('hello', 'world')) # 'hello/world'


if __name__ == '__main__':
    examine_paths()
    #resolve_relative_path()
    #normalize_path()
    #get_filename_with_extension()
    #get_filename_without_extension()
    #get_last_path_component()
    #join_with_empty_string()