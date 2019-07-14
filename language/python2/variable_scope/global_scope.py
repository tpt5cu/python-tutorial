# https://www.programiz.com/python-programming/global-keyword
# https://stackoverflow.com/questions/13881395/in-python-what-is-a-global-statement


"""
Python seems to have 3 scopes: function, class, and global. There is no block scope (if-statements, for-loops, etc.)
- The "global <variable>" statement must go on its own line alone
- Using the "global" keyword outside of a function has no effect.
"""


# Variables created outside of a class or function are global by default
my_global = "default global variable"


class MyClass(object):

    def __int__(self):
        print(my_global)


    def fail_set_global(self):
        my_global = "Fail class set global variable"


    def succeed_set_global(self):
        global my_global
        my_global = "Succeed clas set global variable."


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
    """
    The "global" keyword must be used to read AND write a global variable inside of a function or class.
    """
    print(my_global) # default global variable
    set_global_variable()
    print(my_global) # Changed the global variable


if __name__ == "__main__":
    #class_fail_set_gloabl()
    #class_succeed_set_global()
    fail_set_global_variable()
    #succeed_set_global_variable()