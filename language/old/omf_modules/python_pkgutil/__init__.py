# https://docs.python.org/2/library/pkgutil.html

"""This is the init.py file of my own python_pkgutil package.
What is __name__ doing?
"""

from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)