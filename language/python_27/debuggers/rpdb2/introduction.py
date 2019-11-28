# https://github.com/bluebird75/winpdb/blob/master/rpdb2.py - source code of rpdb2
# http://heather.cs.ucdavis.edu/~matloff/winpdb.html#userpdb2 - rpbd2 tutorial
# https://github.com/bluebird75/winpdb/issues/28 - namespace issue (BROKEN)


import time
from multiprocessing import Process


'''
Unfortunatley when I try to inspect variables, I get "Textual output will be done at the debuggee." This problems makes this debugger effectively
useless.

- Winpdb is the graphical front-end to rpdb2. I'm interested in rpdb2
- Usage: $ python /rpdb2/rpdb2.py introduction.py
    - It opens a separate terminal window, but for whatever reason I should just keep using the original terminal window
- It actually works with multiprocessing code, and I can follow the parent or child!


Breakpoints:
- $ bp <number>
    - Set a breakpoint
- $ bl
    - List breakpoints
- $ bc <number>
    - Clear the breakpoint

Running:
- $ g(o) [[<filename>':'] (<line> | <scope>)]
    - Continue execution until (optionally) a line is reached (or a breakpoint is hit)
- $ n(ext)
    - Continue execution until either the next line in the current function is reached or the function returns
    - Same as pdb
- $ s(tep)
    - Execute the current line and stop at the first possible occasion, which will be either 1) invoking a new function and stopping after going into
      it or 2) stopping on the next line of the current function
- $ exec
    - Execute statement in the context of the current frame
- $ eval
    - Evaluate expression in the context of the current frame
    - 
- $ exit
    - Exit the debugging session
- $ fork [parent | child] [manual | auto]
    - Choose to either follow the parent or child process
    - Additionally, choose whether to always stop before following either one or to just continue down the currently chosen path (i.e. automatically
      follow the parent or automatically follow the child)

Viewing:
- $ l(ist) 
    - list source code (alias for 'list')
- $ up
    - Step up a frame
    - No shorthand
- $ down
    - Step down a frame
    - No shorthand
'''


def spawn_process():
    p = Process(target=print_numbers)
    p.start()
    p.join()


def print_numbers():

    for i in range(10):
        i += 1
        print(i)
        time.sleep(0.5)


if __name__ == "__main__":
    spawn_process()