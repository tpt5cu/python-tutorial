'''
Code control
- $ s
    - execute the current line and stop inside a called function or in the current function
        - This WILL step into function calls
- $ c
    - continue execution until a breakpoint is encountered
        - Why doesn't this skip for-loops? This only happens if a breakpoint is ON a for-loop!
- $ n
    - execute until next line in the function (or the function returns)
        - This will NOT step INTO function calls
- $ unt
    - (usually) only goes to the next line number
- $ j
    - jump around (set the next line that will be executed).
- $ return
    - continue unti the current function returns. Very useful!

Global control
- $ restart
    - Restart the program that is being debugged. Preserve all breakpoints, history, action, debugger options, etc.
    - Unfortunately, sometimes an exception is raised and pdb just exits
- $ exit
    - Abort the program being executed
- $ quit
    - Abort the program being executed
'''