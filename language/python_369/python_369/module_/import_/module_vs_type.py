# This is only allowed at the module level
#from python_369.module_.import_.awesome_module import *


def unresolved_import_with_alias():
    '''
    There is nothing special about combining an unresolved import of a module with an alias. A module object is imported, as expected
    - Actually this is a corner case before Python 3.7 that can cause issues
    '''
    import python_369.module_.import_.awesome_module as awesome_module
    print(type(awesome_module)) # <class 'module'>


def use_local_star_import():
    '''As long as a star import occurs within this module, all imported symbols are visible in the global namespace of this module'''
    awesome_function() # I'm an awesome function!


def trigger_package_level_star_import():
    '''
    A star import in a package import does not add those symbols to THIS module's global namespace. The symbols are visible in whatever module they
    were imported in
    - Since __init__.py performed the * import, those symbols should be visible in the "import_" namespace. This is true!
    - Why was I even confused about this? Because, if a package (i.e. __init__.py) performs a * import, then that package namespace (i.e. "csss")
      directly contains a bunch of symbols (i.e. the class "CSSS"). If I try to import a module (i.e. "CSSS") from the package (i.e. "csss") AND that
      module has the same name as a class that was imported into the __init__.py namespace (i.e. the class "CSSS" that exists in the module "CSSS"),
      then the class (i.e. "CSSS") will SHADOW the module (i.e. "CSSS")
        - This shadowing has nothing to do with classes in particular. It's the fact that the "CSSS" symbol (which happens to contain a class object)
          is resolved from the package namespace directly before the package has to look-up any possibly matching module objects.
    '''
    import python_369.module_.import_
    #awesome_function() # NameError
    # This line here is the point of this example
    python_369.module_.import_.awesome_function() # I'm an awesome function!


if __name__ == '__main__':
    unresolved_import_with_alias()
    #use_local_star_import()
    #trigger_package_level_star_import()
