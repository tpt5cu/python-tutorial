# https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder/50194143#50194143

"""The unfortunate truth is that the built-in Python packages do not have an elegant and robust solution
that allows me to import any file from anywhere in the project directory. Using Python's built-in packages
requires hacking the sys.path and other stuff that is liable to break whenever I move directories around.

The only good solution is to use setuptools, virtual environment, and pip as described in the stack overflow answer.
"""