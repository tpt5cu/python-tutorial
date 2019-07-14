# https://pythonhosted.org/an_example_pypi_project/sphinx.html#function-definitions
# https://stackoverflow.com/questions/15972544/how-to-document-an-exception-using-sphinx
# https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html


"""
Sphinx is a huge and enormously powerful documentation tool for more than just Python. These notes are a tiny subset of the available markup. I will
probably never actually use Sphinx to generate documentation, so my docstrings will be "Sphinx-like" in that they don't conform to exact Sphinx
formatting specifications.
"""


def add_two_numbers(a, b):
    # :param, :type, and :rtype, :raises all seem very useful.
    # :return is useful too
    # the "x or y" syntax is exactly correct for specifiying that something could be multiple types
    """
    Return the sum of two numbers.

    :param a: the first operand.
        add an indent to make Sphinx associated these lines
        with the above un-indented ine.
    :type a: int or float
    :param b: the second operand
    :type b: int or float
    :return: the sum of the two numbers
    :rtype: int or float
    :raises: TypeError, SomeOtherErrorType?
    """
    c = a + b
    return c


if __name__ == "__main__":
    #add_two_numbers("a", 5)
    pass