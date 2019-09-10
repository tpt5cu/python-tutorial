# https://realpython.com/python-debugging-pdb/#essential-pdb-commands
# https://stackoverflow.com/questions/23319883/can-i-view-source-code-of-python-built-in-function-while-debugging-with-pdb


"""
Run pdb non-destructively (i.e. without modifying the source code) with $ python -m pdb <filename>

Commands:
- h: get help. Very useful! All of these commands are much more complex than noted here
- b: list the currently set breakpoints
- b <line number>: insert a breakpoint at <line number>
- b <function name>: insert a breakpoint at <function name>
- l: list 11 lines around the line that currently has been paused
    - Reset the position of l by going up and down the stack
- ll: not defined
- w: print stack trace (most recent frame on bottom)
- u: move upwards one frame
- d: move downwards one frame
    - This will NOT advance the program. It merely moves me around frames
- n: execute until next line in the function (or the function returns)
    - This will NOT step INTO function calls
- s: execute the current line and stop inside a called function or in the current function
    - This WILL step into function calls
- c: continue execution until a breakpoint is encountered
- unt <line number>: continue execution until reaching a line number equal to or greater than <line number>
- clear: clear all breakpoints (after a prompt)
- p <expression>: print the value of <expression>
    - Any valid Python expression will do
- pp <expression>: pretty-print the value of <expression>

If a Python built-in function is written in C, it cannot be stepped into (e.g. sum())
"""


def average_numbers(*args):
    divisor = len(args)
    total = sum(args)
    average = total/float(divisor)
    return average


if __name__ == "__main__":
    avg1 = average_numbers(5, 6, 2, 5, 6)
    avg2 = average_numbers(4.6, 2.5, 56.2, 98.9)
    print("Total: " + str(avg1 + avg2)) # 45.35