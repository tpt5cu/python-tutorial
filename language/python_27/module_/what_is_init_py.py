# https://realpython.com/python-modules-packages/


''' 
When a package is imported, the code in its __init__.py file is run. Remember that a package is imported exactly once during Python execution.
- When a submodule or subpackage of a package is imported, the package is ALSO imported which means package/__init__.py ALSO runs
'''
def foo():
    pass