# https://stackoverflow.com/questions/22241420/execution-of-python-code-with-m-option-or-not


"""
- A python module can be run as a package with $ python -m <module> $. This tells Python to 1) import the module for me and 2) run the imported 
module as a script.
- For example, $ cd ~/tutorials/python && python -m python2.modules_py.imports
    - Note how dots are used instead of slashes
    - Don't include the .py extension in <module>.
    - All directories must have an __init__.py file to indicate that they are modules. If any intermediate directory is missing __init__.py, the
      command won't work
- Running a module as a package allows relative imports to work because Python knows about the structure of the package(s) and can resolve them
    - Without the '-m' flag, Python runs the module as a script and has no concept of if the script is part of a package or not
- The location from which $ python -m <module> $ was run matters.
    - If the command is run beneath directories from which I'm importing, Python won't know about those directories and will throw an error
"""