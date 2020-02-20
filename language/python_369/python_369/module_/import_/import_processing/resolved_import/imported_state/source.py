# https://stackoverflow.com/questions/710551/use-import-module-or-from-module-import


import module_.import_.import_processing.resolved_import.imported_state.observer as observer


def get_symbol_from_module():
    '''
    This line shows that the "import <package>.<package>.<module> as <alias>" syntax does NOT work for "import <package>.<package>.<module>.<symbol>
    as <alias>
    - In other words the ONLY way to get specific symbol from a module is to use the resolved import syntax (i.e. from ...)
    '''
    # ModuleNotFoundError: 'module_.import_.import_processing.resolved_import.imported_state.target' is not a package
    #import module_.import_.import_processing.resolved_import.imported_state.target.do_things as do_things

    # This works, but I'm not getting a specific symbol from the "target" module
    #import module_.import_.import_processing.resolved_import.imported_state.target as target
    #target.do_things() # target.do_things() is doing things!

    # This is sometimes what I'm trying to do, but resolved imports can be dangerous!
    from module_.import_.import_processing.resolved_import.imported_state.target import do_things as x
    x() # target.do_things() is doing things!


def examine_unresolved_import_module_state():
    '''
    When a module is imported with an unresolved import, any modifications to that state of the imported module will be visible to other importing
    modules, e.g.:
        - Changes to target.target_list will be externally visible EVERYWHERE
        - Changes to target.target_var will be externally visible EVERYWHERE
    '''
    import module_.import_.import_processing.resolved_import.imported_state.target as target
    print(target.target_list) # ['foo']
    target.target_list.append('bar')
    target.target_var = 'bar'
    # Unresolved observer import sees: ['foo', 'bar']
    # Unresolved observer import sees: bar
    observer.unresolved_import() 
    # Resolved observer import sees: ['foo', 'bar']
    # Resolved observer import sees: bar
    observer.resolved_import() 
    

def examine_resolved_import_module_state():
    '''
    Everything in Python is an object. A variable is a reference to an object.
    - When a mutable object (i.e. target_list) is modified through an unresolved import (see above) or a resolved import (see below), only a SINGLE
      object is being modified, and those changes are visible to all other importing modules
        - What I think actually happens is:
            1) An import makes Python copy the value of a reference into this namespace
            2) That reference is shared across all modules
            3) A mutable object can be changed through its reference
            4) Therefore, all modules will change the same mutable object through identical copies of the same reference
    - It is different for immutable objects:
        - When an immutable object (i.e. target_var) is modified through an unresolved import (see above):
            1) This namespace never got a reference to "target_var" directly
            2) It can only modify "target_var" though "target"
            3) Thus, when "target.target_var" is performed, the ACTUAL target_var is looked-up and modified and those changes are visible everywhere
               - The original target.target_var has its reference changed to a new object and that new object is visible everywhere
        - When an immutable object (i.e. target_var) is modified through a resolved import (see below):
            1) This namespace got a copy of the value of the reference to "target_var"
            2) Python knows that immutable objects can't be changed
            3) When "target_var" is modified here, what actually happens is that a new object immutable object is created in memory and "target_var"
               becomes a NEW reference to the NEW object
            4) Thus, when "target_var" is modified, those changes are not visible to external modules who import the original "target.target_var" and
               thus still possess a reference to the original mutable object
    '''
    from module_.import_.import_processing.resolved_import.imported_state.target import target_list
    from module_.import_.import_processing.resolved_import.imported_state.target import target_var
    print(target_list) # ['foo']
    target_list.append('bar')
    target_var = 'bar'
    # Unresolved observer import sees: ['foo', 'bar']
    # Unresolved observer import sees: foo
    observer.unresolved_import()
    # Resolved observer import sees: ['foo', 'bar']
    # Resolved observer import sees: foo
    observer.resolved_import()


if __name__ == '__main__':
    #get_symbol_from_module()
    #examine_unresolved_import_module_state()
    examine_resolved_import_module_state()
