"""
https://stackoverflow.com/questions/11949808/what-is-the-difference-between-a-function-an-unbound-method-and-a-bound-method/26943327
"""

"""
A function object is created by a def statement or a lambda expression. When a function appears within the body of a class statement, it is
transformed into an "unbound method" (only in Python 2. Python 3 doesn't have unbound methods).
    - Invoking an unbound method from a class instance transforms it into a bound method. A bound method merely supplies the class instance to itself
      as the first parameter, which is conventionally called "self"
    - 

"""