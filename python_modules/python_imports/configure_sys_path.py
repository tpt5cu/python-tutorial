# https://www.programiz.com/python-programming/global-keyword
# http://ask.xmodulo.com/change-syspath-pythonpath-python.html
# https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html


"""SimpleNamespace doesn't exist in Python 2, use type() instead"""
#from types import SimpleNamespace
import sys

"""I'm making op into a dummy custom object so I can add attributes to it"""
#op = SimpleNamespace()
op = type("CustomClassObject", (), {})


def import_my_add():
    """I'm importing module 'adding' from package 'python_operators'. Note that this actual import just places the module
    into the scope of THIS function. The imports are wrapped in a function just for the sake of this tutorial
    """
    import python_operators.adding as my_add
    #import python_operators.equality
    """This line won't work unless 'op' is actually defined at the global level."""
    global op
    """I'm adding my_add to the global scope so I can use it in other functions (to pretend as if I had imported
    my_add normally at the top of the file"""
    op.adding = my_add


def import_module_from_package():
    import_my_add()
    """As long as a package is within the search path, specific modules can be imported from that package.
    Note that importing a package alone does NOT make all the modules available. The desired modules must
    specifically be imported.
    """
    op.adding.plus_equals_with_mutable_object()
    """This throws an AttributeError because module 'python_operators' has no attribute 'equality'"""
    #op.equality


def tricky_import_package():
    import_my_add()
    """When this file is run from my IDE, /Users/autinchang/pycharm/python_tutorial is in the search path (it's the
    PYTHONPATH environment variable). That means all packages within what I consider to be the root
    directory are available for importing in any of my scripts.

    When this file is run from my terminal, the search path does NOT include the above path. That means I get
    ImportError when running this script in the terminal!
    """
    op.adding.regular_plus_with_mutable_object()
    #print(op.adding.__file__)


def brittle_fix_import_errors():
    """The first way to correct an import error is to explicitly modify sys.path inside my code. This is temporary
    and brittle. Now the import will work as expected, but ONLY in THIS function! Note how the sys.path must be
    modified BEFORE the import happens in order for Python to find the desired module.
    """
    sys.path.append("/Users/austinchang/pycharm/python_tutorial")
    import python_operators.equality
    python_operators.equality.equals_operator()


if __name__ == "__main__":
    #import_module_from_package()
    #tricky_import_package()
    brittle_fix_import_errors()
