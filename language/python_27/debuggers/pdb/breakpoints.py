# https://realpython.com/python-debugging-pdb/#using-breakpoints

'''
View breakpoints
- $ b
    - This is supposed to list all of the breakpoints
    - tbf, perhaps if I'm using "import pdb; pdb.settrace()", those types of breakpoints aren't listed?
Set a breakpoint
- $ b(reak) ([file:]lineno | function) [, condition]
    - It appears that a filename and function name can't be used together. Only a filename and lineno may be used together
    - Yes conditional breakpoints are allowed. Just look at the syntax!
    - To set a breakpoint in an external file, use slashes in a path that is relative to something in sys.path
        - E.g. $ b omf/cymeToGridlab.py:134 

Delete a breakpoint
- $ cl <breakpoint number>: remove the specified breakpoint
    - Without space-separated number arguments, 'cl' will clear all breakpoints

Disable/enable a breakpoint
- $ disable <breakpoint number>
- $ enable <breakpoint number>
'''
