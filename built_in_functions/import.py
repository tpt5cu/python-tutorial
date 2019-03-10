# https://docs.python.org/2/library/functions.html#__import__

"""See the "python_modules" package for how to import package and find files. """

"""
The __import__() built-in function is invoked by the import statement. It is mainly used to import a module
whose name is only known at run-time.
I've also seen it used to eliminate the need for a separate import statement, followed by other code, by using the
returned value (a namespace) to access stuff from inside the namespace (e.g. call a function)
"""