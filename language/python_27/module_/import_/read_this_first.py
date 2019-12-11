# https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html - good, but not perfect, introduction
# https://stackoverflow.com/questions/7850908/what-exactly-should-be-set-in-pythonpath - PYTHONPATH
# https://www.python.org/dev/peps/pep-0328/ - usage of __name__


import sys


'''
- sys.path is list of strings, where each string represents a directory where Python modules can be found.
- sys.path is used to find and import packages, which can exist in a wide variety of locations. These locations include (in no particular order)
    - Packages that are built-in to the interpreter
    - Other installation-dependent file system directories where packages are known by Python to be installed
    - Packages in directories specified by PYTHONPATH (which is usually unset)
    - Packages that are relative to the script that is used as the main entrypoint
        - sys.path[0] is either an absolute directory (no -m flag) or an empty string (-m flag)
- There IS a specific ordering of sys.path, and a package that is found earlier in the list will resolve before a package with the same name that is
  found later in the list, but the specific ordering depends on whether or not the -m flag is used
    - See the "m_flag" and "no_m_flag" notes for important details
    - In a nutshell, the ordering of sys.path (and consequently, the resolution order of packages) is:
        1) The directory containing the main entry point script
        2) Directories in PYTHONPATH
        3) Installation-dependent list of directories
- The __name__ of a module is used to:
    - Provide a unqiue namespace for every module
    - More? (Is it used to resolve import themselves as an implementation detail? I'm not sure)

__name__: 
- Relative imports use a module's __name__ attribute to determine that module's position in the package hierarchy. If the module's name does not
  contain any package information (e.g. it is set to '__main__') then relative imports are resolved as if the module were a top level module,
  regardless of where the module is actually located on the file system.

No -m flag:
- The main Python entry point module is run as a script.
    - Explicit relative imports are not possible
- Only "absolute import syntax" is possible. However, packages relative to the main entry point module can still be imported with absolute import
  syntax because the syntax also doubles as implicit relative import sytnax that looks-up packages relative to the main entry point script
- The __name__ of an imported package/module is always the same, no matter where $ python $ is run from. The base of the name is always the
  package/module that exists in the same directory as the main entry point script
    - E.g. $ python module_/import_/read_this_first.py $: cool_stuff.__name__ == m_flag.cool_stuff
    - This makes sense because sys.path[0] is the absolute path of the main entry point script's directory. That directory will always contain
      packages/modules that are next to the main entry point script. Thus, this form of __name__ can always be resolved relative to sys.path[0]

-m flag:
- The main Python entry point module is first imported, then it is run as a script
    - More specifically, a "package context" is created which imports all of the specified packges and then the script is run within the packaged
      context
    - Explicit relative imports are possible, so long as they only move around the package context
- The __name__ of an imported package/module changes depending on the created "package context." The base of __name__ is always the root of the
  package context, so that the imported module can be resolved relative to the root of the package context.
    - E.g. $ python -Bm module_.import_.read_this_first $: cool_stuff.__name__ == module_.import_.m_flag.cool_stuff
'''


def understanding_name():
    '''
    - When a Python module (i.e. read_this_first.py) is run as the main entry point to the application, __name__ is always '__main__', regardless of
      whether or not the -m flag was used
    - When a Python module (i.e. m_flag.cool_stuff) is imported, its __name__ depends on whether or not the -m flag was used:
        - $ python -Bm module_.import_.read_this_first $: cool_stuff.__name__ == module_.import_.m_flag.cool_stuff
            - The -m flag was used, so Python imports all of the specified packages, then runs the main entry point.
            - The "cool_stuff" module's name is relative to the base of the package hierarchy, BUT "cool_stuff" MUST be imported exactly as
              "m_flag.cool_stuff" because sys.path[0] == "" means that only THIS directory in the entire packaged context will be searched, and
              "m_flag" exists in THIS directory while "cool_stuff" does not
                - In other words, "import cool_stuff" and "import import_.m_flag.cool_stuff" aren't valid
        - $ python module_/import_/read_this_first.py $: cool_stuff.__name__ == m_flag.cool_stuff
            - The -m flag was not used, so Python runs this file as a script. The cool_stuff module's name is relative to the package whose parent
              directory was found in sys.path
    '''
    #for p in sys.path:
    #    print(p)
    import m_flag.cool_stuff as mod
    print(__name__) # __main__
    print(mod.__name__) # <depends on how Python was run>


if __name__ == '__main__':
    understanding_name()