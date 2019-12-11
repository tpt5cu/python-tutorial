# https://stackoverflow.com/questions/22241420/execution-of-python-code-with-m-option-or-not
# https://www.python.org/dev/peps/pep-0328/ - bearable summary of new (explicit) relative import syntax
# https://stackoverflow.com/questions/11536764/how-to-fix-attempted-relative-import-in-non-package-even-with-init-py - parent must be in path to use
# explicit relative imports


'''
- Remember to use "." paths instead of "/" in the command-line
- The reason all of this behavior works like this is because the -m flag makes Python import the package or module for me into its own context, then
  run the module as a script
    - Without the -m flag, Python just runs a module as a script
- See the second source listed above for all of the ways to write explicit relative imports
    - Remember that each "." represents one directory level
        - "." is the same directory as this script
        - ".." is the parent directory of this script
        - "..." is the grandparent directory of this script
'''


def use_shadowed_site_packages_package():
    ''''
    When Python is run with the -m flag, regular site-packages packages can be shadowed. This is because:
    - The first entry in sys.path is "", which directs Python to search the directory of this script for a matching package or module. Python finds
      the local "io" package and uses it
        - This is true regardless of where $ python -Bm [<other modules in path>.]<module name> $ was run
    '''
    import io
    with io.open('__init__.py') as f: # AttributeError: 'module' object has no attribute 'open'
        print(type(f))


def use_shadowed_built_in_package():
    '''The above behavior is exactly the same for special built-in packages '''
    import sys
    # These are the packages that are compiled into the interpreter, of which "sys" is one
    #print(sys.builtin_module_names)
    print(sys.path) # AttributeError: 'module' object has no attribute 'path'


def generous_relative_import_module():
    '''
    This import works regardless of where $ python -Bm [<other modules>.]<module name> $ was run
    - Why? Presumably because if this module is run without a surrounding "package context", then this import is treated as an absolute import and is
      resolved according to the first matching entry in sys.path
    - This type of import is called an "implicit relative import" but I'm not sure that's a great name because is it really being treated as a
      relative import when used in this way?
    '''
    from cool_stuff import do_cool_stuff
    do_cool_stuff()


def picky_relative_import_module():
    '''
    This import only works if $ python -Bm ... <module name> $ runs this module within a "package context". What I mean by this is that "python -Bm
    ..." must be run at least one directory above the directory of this module. This must be necessary because an explicit relative import requires a
    package context to resolve an (explicit) relative import
    - E.g $ python -Bm import_.m_flag.introduction $ and $ python -Bm m_flag.introuction $ both work but $ python -Bm introduction $ doesn't work
    - This type of import is called an "explicit relative import". This makes sense because the syntax is 1) always treated as a real relative import
      and 2) fails fast as it should
    '''
    from .cool_stuff import do_cool_stuff
    do_cool_stuff()


if __name__ == '__main__':
    #use_shadowed_built_in_package()
    #use_shadowed_site_packages_package()
    #generous_relative_import_module()
    picky_relative_import_module()