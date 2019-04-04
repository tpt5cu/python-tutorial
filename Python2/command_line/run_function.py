"""
python -c "import omf.feeder; print(omf.feeder.parse('/Users/austinchang/Downloads/hardware - underground line conductors.glm'))"

The above line is an example of how to run a python file, or part of it, from the command line.
    - The "-c" flag runs python with the command flag
    - Next, the relevant module is imported from the omf package
    - The parse() function doesn't print anything itself, so I must wrap the function call in a print() function if I want to see the output in my terminal
    - I must fully qualify the parse() function, since I used the <package>.<module> style of import. I wouldn't necessarily have to do this if i used a different import style
    - I made sure to use single-quoted strings for the file path since the entire command is surrounded in double-quotes
    - profit

    - The output of this file is a straight-up JavaScript object of objects (i.e. a Python dictionary of dictionaries). Each dictionary needs to go into its own component.json file.
    - Remember that the os.getcwd() prints the directory from which the command was run, NOT the directory within which the file is contained. This indicates that it MATTERS which directory the "python" command was executed in. This can cause extremely annoying bugs when Python modules are written in such a way that they break if executed from different directories on the command-line
"""
