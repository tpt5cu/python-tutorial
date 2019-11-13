# https://stackoverflow.com/questions/13872049/print-empty-line


"""
Python 3 print() prints a newline, as I want. Python2 "print()" prints "()" which is NOT what I want.
"""


def python2_print_newline():
    print("Hi")
    # Looks weird but is correct for Python 2. This simply references the function "print" in Python 3 and does not do anything
    print
    print("Bye")


def python3_print_newline():
    print("Hi")
    # Prints "()" in Python 2 which is annoying
    print()
    print("Bye")


def python2_and_3_newline():
    print("Hi")
    # This works for both Python 2 and Python 3, so do it
    print("")
    print("Bye")

if __name__ == "__main__":
    python2_print_newline()
    print("\n")
    python3_print_newline()
    print("\n")
    python2_and_3_newline()