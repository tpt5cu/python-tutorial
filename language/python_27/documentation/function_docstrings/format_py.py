# https://www.python.org/dev/peps/pep-0257/


import sphinx_content


"""
There are two forms of docstrings: single and multi-line. I should use # comments for URLs because I don't want the URLs to form the docstring for a module!
"""


def add_two_numbers(a, b):
    """Add two numbers and return number."""
    # There is no space after the opening """ or before the closing """
    # Single-line docstrings should be entirely on one line
    # The docstring ends in a period. It should read as "the effect of a command" as opposed to "a description of what will happen"
    # Good: """Return the sum of two numbers."""
    # Bad: """Returns the sum of two numbers."""
    # Best: """Add two numbers and return an int or float."""
    # The docstring is never a function signature (e.g. add_two_numbers(int, int) -> int) because the signature can be obtained with introspection
    # However, the return value cannot be determined by introspection, so it should be mentioned
    return a + b


def do_something_complicated(index, rows, url, probability):
    """
    Return the result of the complex operation as a float.

    <not specified by official documentation>
    """
    # A multi-line docstring should also have a summary line at the very top. The summary line can be on the same line as the opening quotes or on the
    # next line.
    # The summary line must be separated by a BLANK line from the rest of the doctring.
    # The official Python documentation does not list HOW exceptions, behavior, arguments, etc. should be described in a multi-line docstring; that's
    # where Sphynix comes in
    # The closing quotations should go on their own line
    pass


def view_docstrings():
    #print(add_two_numbers.__doc__)
    #print(do_something_complicated.__doc__)
    print(sphinx_content.__doc__)


if __name__ == "__main__":
    view_docstrings()