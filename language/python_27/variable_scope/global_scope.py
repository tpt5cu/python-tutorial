# https://www.programiz.com/python-programming/global-keyword
# https://stackoverflow.com/questions/13881395/in-python-what-is-a-global-statement


"""
- Python seems to have 3 scopes: function, class, and global. There is no block scope (if-statements, for-loops, etc.)
    - There's also scope within with-statements
- The "global <variable>" statement must go on its own line alone
- Using the "global" keyword outside of a function has no effect.
"""


# Variables created outside of a class or function are global by default
my_global = "default global variable"


def read_global_variable():
    """A global variable can be read just fine"""
    print(my_global) # default global variable


def write_global_variable():
    """
    Assigning a global variable inside of a function actually creates a local variable that shadows the global variable. Once the shadowing local
    variable has been created, the global variable cannot be accessed
    """
    global my_global
    print(my_global) # default global variable
    my_global = 'local variable'
    print(my_global) # local variable
    global my_global
    print(my_global) # local variable


class MyClass(object):

    def __int__(self):
        print(my_global)


    def fail_set_global(self):
        my_global = "Fail class set global variable"


    def succeed_set_global(self):
        global my_global
        my_global = "Succeed class set global variable."


def class_fail_set_gloabl():
    print(my_global) # default global variable
    obj = MyClass()
    obj.fail_set_global()
    print(my_global) # default global variable


def class_succeed_set_global():
    print(my_global) # default global variable
    obj = MyClass()
    obj.succeed_set_global()
    print(my_global) # Succeed class set global variable


def set_local_variable():
    """
    Variables created inside of a class or function are local by default. This local variable happens to be shadowing a global variable. The global
    variable does not change because I never modify it.
    """
    my_global = "something else"


def set_global_variable():
    global my_global
    my_global = "Changed the global variable"


def fail_set_global_variable():
    print(my_global) # default global variable
    # Writing this line below makes the above line throw an UnboundLocalError because Python sees that I create a local variable called "my_global",
    # and that the print statement is trying to use this local variable. Without this line below, Python sees no local variable called "my_global" and
    # so knows to automatically check the higher scope (which happens to be global) for the variable.
    #my_global = 5
    set_local_variable()
    print(my_global) # default global variable


def succeed_set_global_variable():
    """The "global" keyword must be used to read AND write a global variable inside of a function or class."""
    print(my_global) # default global variable
    set_global_variable()
    print(my_global) # Changed the global variable


if __name__ == "__main__":
    #read_global_variable()
    write_global_variable()
    #class_fail_set_gloabl()
    #class_succeed_set_global()
    #fail_set_global_variable()
    #succeed_set_global_variable()