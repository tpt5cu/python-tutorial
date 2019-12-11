'''
I don't show examples of attemping explicit relative imports here because such syntax isn't allowed when Python is run without the -m flag
'''


def use_shadowed_site_packages_package():
    '''
    When Python is run without the -m flag, regular site-packages packages can be shadowed. This is because:
    1) The first item in sys.path is '/Users/austinchang/tutorials/python/language/python_27/module_/import_/no_m_flag'. This directory will be
       searched first when Python is trying to resolve an import statement
    2) "io" is not a special built-in package, so it can be shadowed
    '''
    import io
    with io.open('__init__.py') as f: # AttributeError: 'module' object has no attribute 'open'
        print(type(f))


def use_shadowed_built_in_package():
    '''
    When Python is run without the -m flag, built-in packages cannot (easily) be shadowed. This is because:
    - Python just happens to first search the built-in packages that are part of the interpreter when Python is run without the -m flag
        - As shown above, regular site-packages packages can be shadowed even when Python is run without the -m flag, but built-in packages are
          special in this mode
    '''
    # For built-in packages, this can be thought of as always being an absolute import when Python is run without the -m flag 
    #   - It's a special case and it's confusing, but it's true. Logically, "sys" should be shadowed due to the ordering of sys.path, but it just isn't
    import sys
    # These are the packages that are compiled into the interpreter, of which "sys" is one
    #print(sys.builtin_module_names)
    print(sys.path) # Big list


if __name__ == '__main__':
    use_shadowed_built_in_package()
    use_shadowed_site_packages_package()